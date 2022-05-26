import os



filePath = os.path.abspath("./OsPath.py")

dirPath1 = os.path.abspath(".")

dirPath2 = os.path.abspath(".") + "/"



print

print "test abspath begin"

print "filePath:", filePath

print "dirPath1:", dirPath1

print "dirPath2:", dirPath2

print "test abspath end"



print

print "test basename begin"

print os.path.basename(filePath)

print os.path.basename(dirPath1)

print os.path.basename(dirPath2)

print "test basename end"



print

print "test dirname begin"

print os.path.dirname(filePath)

print os.path.dirname(dirPath1)

print os.path.dirname(dirPath2)

print "test dirname end"



print

print "test commonprefix begin"

pathList = [filePath, dirPath1, dirPath2]

print os.path.commonprefix(pathList)

pathList.append(os.path.dirname(dirPath1))

print os.path.commonprefix(pathList)

print "test commonprefix end"



print

print "test exists begin"

print os.path.exists(filePath)

print os.path.exists(dirPath1)

print os.path.exists(dirPath2)

print "test exists end"



print 

print "test expanduser begin"

print os.path.expanduser("~/xxx")

print "test expanduser end"



print

print "getatime"

print os.path.getatime(filePath)

print os.path.getatime(dirPath2)



print

print "getmtime"

print os.path.getmtime(filePath)

print os.path.getmtime(dirPath2)



print

print "getctime"

print os.path.getctime(filePath)

print os.path.getctime(dirPath2)



print

print "getsize"

print os.path.getsize(filePath)

print os.path.getsize(dirPath2)



print

print "isabs"

print os.path.isabs(filePath)

print os.path.isabs("~/python")



print

print "isfile isdir islink ismount"

print os.path.isfile(filePath)

print os.path.isdir(filePath)

print os.path.islink(filePath)

print os.path.islink(filePath)



print 

print "join"

print os.path.join("~", "python")

print os.path.join("xxx", "yyy")



print 

print "normpath"

print os.path.normpath("~/python/../code")

print os.path.normpath("aa/bb/cc/../dd/")



print 

print "realpath"

print os.path.realpath(".")

print os.path.realpath(filePath)

print os.path.realpath("aa/bb/cc/../dd/")



print 

print "relpath"

print os.path.relpath(os.path.dirname(dirPath1))



print

print "split"

print os.path.split(filePath)

print os.path.split(dirPath1)

print os.path.split(dirPath2)



print 

print "splitdirve"

print os.path.splitdrive(filePath)



print 

print "splitext"

print os.path.splitext(filePath)

print os.path.splitext(dirPath1)

print os.path.splitext(dirPath2)



print

print "test walk begin"

def TestWalkVisit(fileList, dirName, names):

	for name in names:

		fileList.append(os.path.join(dirName, name))

		print dirName, ":", name

		if os.path.isdir(name):

			print "del dir"

			removedDirs.append(name)



fileList = []

os.path.walk("/home/xiaol_luo/python", TestWalkVisit, fileList)

print fileList

print "test walk end"

