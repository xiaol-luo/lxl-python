import string
import os
import sys

workDir = os.getcwd()
if len(sys.argv) > 2:
    workDir = sys.argv[2]
print("workDir{0}".format(workDir))

os.chdir(workDir)

linkDirMap = {
    "examples/try-lua-protobuf/external/lua5.3": "examples/lua-5.3.4/src",
    "examples/try-lua-protobuf/external/protobuf": "examples/protobuf/src",
    "examples/try-lua-protobuf/external/libs": "ws/output",
    "ws/try-lua-protobuf/luamsg/script": "examples/try-lua-protobuf/luamsg/script",
    "git-dir/lxl-cpp-code/try-libevent/3rdpart/libevent/include": "git-dir/Libevent/WIN32-Code/nmake", 
    "git-dir/lxl-cpp-code/try-libevent/3rdpart/libevent/libs": "git-ws/libevent/lib",
    'git-dir/lxl-cpp-code/try-libevent/3rdpart/common/include': 'git-dir/lxl-cpp-code/common',
    'git-dir/lxl-cpp-code/try-libevent/3rdpart/common/libs': 'git-ws/common',
}

def RemoveLink():
    for link, dir in linkDirMap.items():
        absLinkPath = os.path.abspath("{0}/{1}".format(workDir, link))
        if os.path.exists(absLinkPath):
            os.remove(absLinkPath)
        print("remove link {0}".format(absLinkPath))

def CreateLink():
    RemoveLink()
    for link, dir in linkDirMap.items():
        absDirPath = os.path.abspath("{0}/{1}".format(workDir, dir))
        if not os.path.isdir(absDirPath):
            print("{0} is not a dir".format(absDirPath))
            exit(-1)
        absLinkPath = os.path.abspath("{0}/{1}".format(workDir, link))
        print("create link {0}={1}".format(absLinkPath ,absDirPath))
        os.symlink(absDirPath, absLinkPath)

methodMap = {
    "create": CreateLink,
    "remove" : RemoveLink
}

methodMap[sys.argv[1]]()
