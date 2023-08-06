# -*- coding: utf-8 -*-
# cython:language_level=3
"""
-------------------------------------------------
   File Name：     lbcBase
   Description :
   Author :       liaozhaoyan
   date：          2021/7/20
-------------------------------------------------
   Change Activity:
                   2021/7/20:
-------------------------------------------------
"""
__author__ = 'liaozhaoyan'

import sys
import os
import base64
import ctypes as ct
import _ctypes as _ct
import json
import hashlib
from pylcc.lbcMaps import CmapsEvent, CmapsHash, CmapsArray, \
    CmapsLruHash, CmapsPerHash, CmapsPerArray, CmapsLruPerHash, CmapsStack
from surftrace.execCmd import CexecCmd
from surftrace.surfException import InvalidArgsException, RootRequiredException, FileNotExistException, DbException
from surftrace.lbcClient import ClbcClient

LBC_COMPILE_PORT = 7655
SEG_UNIT = 4096


def segDecode(stream):
    line = b""
    l = len(stream)
    for i in range(0, l, 4 * SEG_UNIT):
        s = stream[i:i + 4 * SEG_UNIT]
        line += base64.b64decode(s)
    if l % (4 * SEG_UNIT):
        i = int(l / (4 * SEG_UNIT) * (4 * SEG_UNIT))
        line += base64.b64decode(stream[i:])
    return line


class ClbcBase(object):
    def __init__(self, bpf, bpf_str="",
                 server="pylcc.openanolis.cn",
                 arch="", ver="", env="",
                 workPath=None, logLevel=-1):

        if "LBC_SERVER" in os.environ:
            server = os.environ["LBC_SERVER"]
        if "LBC_LOGLEVEL" in os.environ:
            logLevel = int(os.environ["LBC_LOGLEVEL"])
        if workPath:
            self._wPath = workPath
        else:
            self._wPath = os.getcwd()
        super(ClbcBase, self).__init__()
        self.__need_del = False
        self._server = server
        self._c = CexecCmd()
        self._checkRoot()
        self._env = env
        self._logLevel = logLevel

        if ver == "":
            ver = self._c.cmd('uname -r')
        if arch == "":
            arch = self._c.cmd('uname -m')
        self._checkBtf(ver, arch)
        bpf_so = self._getSo(bpf, bpf_str, ver, arch)

        self._loadSo(bpf_so)
        self.maps = {}
        self._loadMaps()

    def __del__(self):
        if self.__need_del:
            self.__so.lbc_bpf_exit()

    def _checkBtf(self, ver, arch):
        if os.path.exists('/sys/kernel/btf/vmlinux'):
            return
        name = "/boot/vmlinux-%s" % ver
        if not os.path.exists(name):
            cli = ClbcClient(server=self._server, ver=ver, arch=arch)
            dRecv = cli.getBtf()
            if dRecv['btf'] is None:
                print("get btf failed, log is:\n%s" % dRecv['log'])
                raise InvalidArgsException("get btf failed.")
            print("get btf from remote success.")
            with open(name, 'wb') as f:
                f.write(segDecode(dRecv['btf']))

    @staticmethod
    def _closeSo(so):
        _ct.dlclose(so._handle)

    def _getSo(self, bpf, s, ver, arch):
        bpf_so = self._wPath + '/' + bpf + ".so"
        need = False
        if s == "":
            bpf_c = self._wPath + '/' + bpf + ".bpf.c"
            if self._checkCCompile(bpf_c, bpf_so, ver, arch):
                with open(bpf_c, 'r') as f:
                    s = f.read()
                need = True
        else:
            need = self._checkStrCompile(s, bpf_so, ver, arch)
        if need:
            self._compileSo(s, bpf_so, ver, arch)
        return bpf_so

    def _checkCCompile(self, bpf_c, bpf_so, ver, arch):
        cFlag = os.path.exists(bpf_c)
        oFlag = os.path.exists(bpf_so)
        if not (cFlag or oFlag):  # is not exist
            raise FileNotExistException("bpf.c or so is not in this dictionary.")
        elif not oFlag and cFlag:  # only bpf.c
            return True
        elif oFlag and not cFlag:  # only so, should check version
            if self._checkVer(bpf_so, ver, arch):
                raise FileNotExistException("bad bpf.so and not bpf.c")
            return False
        else:  # both bpf.c and bo, check hash and version
            with open(bpf_c, "r") as f:
                s = f.read()
            if sys.version_info.major >= 3:
                cHash = hashlib.sha256(s.encode()).hexdigest()
            else:
                cHash = hashlib.sha256(s).hexdigest()
            if self._checkHash(bpf_so, cHash):
                return True
            return self._checkVer(bpf_so, ver, arch)

    def _checkStrCompile(self, s, bpf_so, ver, arch):
        oFlag = os.path.exists(bpf_so)
        if not oFlag:  # only string
            return True
        else:  # both bpf.c and bo, check hash and version
            if sys.version_info.major >= 3:
                cHash = hashlib.sha256(s.encode()).hexdigest()
            else:
                cHash = hashlib.sha256(s).hexdigest()
            if self._checkHash(bpf_so, cHash):
                return True
            return self._checkVer(bpf_so, ver, arch)

    def _parseVer(self, ver):
        major, minor, _ = ver.split(".", 2)
        return major

    def _checkVer(self, bpf_so, ver, arch):
        """if should compile return ture, else return false"""
        try:
            so = ct.CDLL(bpf_so)
        except (OSError, FileNotFoundError):
            return True
        so.lbc_get_map_types.restype = ct.c_char_p
        so.lbc_get_map_types.argtypes = []
        s = so.lbc_get_map_types()
        soVer = json.loads(s)['kern_version']
        self._closeSo(so)

        soMajor = self._parseVer(soVer)
        hMajor = self._parseVer(ver)
        return (int(soMajor) > 3) ^ (int(hMajor) > 3)

    def _checkHash(self, bpf_so, cHash):
        """if should compile return ture, else return false"""
        try:
            so = ct.CDLL(bpf_so)
        except (OSError, FileNotFoundError):
            return True
        so.lbc_get_map_types.restype = ct.c_char_p
        so.lbc_get_map_types.argtypes = []
        s = so.lbc_get_map_types()
        soHash = json.loads(s)['hash']
        self._closeSo(so)
        return not cHash == soHash

    def _checkRoot(self):
        cmd = 'whoami'
        line = self._c.cmd(cmd).strip()
        if line != "root":
            raise RootRequiredException('this app need run as root')

    def _compileSo(self, s, bpf_so, ver, arch):
        cli = ClbcClient(server=self._server, ver=ver, arch=arch, port=LBC_COMPILE_PORT)
        dRecv = cli.getC(s, self._env)
        if dRecv is None:
            raise Exception("receive error")
        if dRecv['so'] is None:
            print("compile failed, log is:\n%s" % dRecv['clog'])
            raise InvalidArgsException("compile failed.")
        print("remote server compile success.")
        with open(bpf_so, 'wb') as f:
            f.write(segDecode(dRecv['so']))

    def _loadSo(self, bpf_so):
        self.__need_del = True
        self.__so = ct.CDLL(bpf_so)
        self.__so.lbc_bpf_init.restype = ct.c_int
        self.__so.lbc_bpf_init.argtypes = [ct.c_int]
        r = self.__so.lbc_bpf_init(self._logLevel)
        if r != 0:
            self.__need_del = False
            raise InvalidArgsException("so init failed")

    def _loadMaps(self):
        self.__so.lbc_get_map_types.restype = ct.c_char_p
        self.__so.lbc_get_map_types.argtypes = []
        s = self.__so.lbc_get_map_types()
        d = json.loads(s)['maps']
        tDict = {'event': CmapsEvent,
                 'hash': CmapsHash,
                 'array': CmapsArray,
                 'lruHash': CmapsLruHash,
                 'perHash': CmapsPerHash,
                 'perArray': CmapsPerArray,
                 'lruPerHash': CmapsLruPerHash,
                 'stack': CmapsStack, }
        for k in d.keys():
            t = d[k]['type']
            if t in tDict:
                self.maps[k] = tDict[t](self.__so, k, d[k])
            else:
                raise InvalidArgsException("bad type: %s, key: %s" % (t, k))


class ClbcApp(ClbcBase):
    def __init__(self, soPath):
        super(ClbcApp, self).__init__(soPath)

    def _callback(self, cpu, data, size):
        stream = ct.string_at(data, size)
        e = self.maps['my_map'].event(stream)
        print("%d, %s, 0x%x" % (e.pid, e.comm, e.cookie))
        tbl = self.maps['pids'].get()
        if len(tbl) > 20:
            self.maps['pids'].clear()
        print(self.maps['callStack'].getStacks(e.stack_id, 2))

    def loop(self):
        self.maps['my_map'].open_perf_buffer(self._callback)
        try:
            self.maps['my_map'].perf_buffer_poll()
        except KeyboardInterrupt:
            print("key interrupt.")
            exit()


if __name__ == "__main__":
    a = ClbcApp('lbc')
    a.loop()