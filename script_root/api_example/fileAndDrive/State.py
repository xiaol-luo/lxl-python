import os
import stat

filePath = os.path.abspath("./State.py")
dirPath = os.path.dirname(filePath)

fileStat = os.stat(filePath)
dirStat = os.stat(dirPath)

print fileStat
print dirStat

print stat.S_ISDIR(fileStat)
