import os

def OpenFile(path, mode, autoCreate=False):
	if autoCreate:
		if not os.path.exists(path):
			with open(path, "w") as f:
				pass
	if os.path.isfile(path):
		f = open(path, mode)
		return f;
	return None;


filePath = os.path.abspath("data.txt")
if os.path.exists(filePath) and os.path.isfile(filePath):
	os.remove(filePath)

f = OpenFile(filePath, "r+", True)

if not f:
	os.abort()


print f
print "fileno", f.fileno()
print "isatty", f.isatty()
print "mode", f.mode
print "name", f.name
print "newline", f.newlines
print "tell", f.tell()

f.write("1234567890" * 3 + os.linesep)
print "tell", f.tell()

strList = []
strList.append("strList line 1" + os.linesep)
strList.append("strList line 2" + os.linesep)
strList.append("strList line 3" + os.linesep)
f.writelines(strList)
print "tell", f.tell()


f.seek(-5, os.SEEK_CUR)
f.truncate()
f.flush();
print "tell", f.tell()
f.close()

f = OpenFile(filePath, "r", False)
if not f:
	os.abort()

f.seek(0, os.SEEK_END)
print "tell", f.tell()

print
print "test read all"
f.seek(0, os.SEEK_SET)
print f.read()

print
print "test read(20)"
f.seek(0, os.SEEK_SET)
print f.read(20)
print f.read(20)
print "tell", f.tell()

print
print "test loop read line"
f.seek(0, os.SEEK_SET)
for line in f:
	print line,
print "tell", f.tell()

print
print "test readline"
f.seek(0, os.SEEK_SET)
print f.readline()
print f.readline()
print "tell", f.tell()

print
print "test readline(25)"
f.seek(0, os.SEEK_SET)
print f.readline(25)
print "tell", f.tell()
print f.readline(25)
print "tell", f.tell()
print f.readline(25)
print "tell", f.tell()
print f.readline(25)
print "tell", f.tell()
print "test realine end"
print "readline return either hit os.linesep|EOF or 25 charater. the return string contain os.lineseq"


print
print "test readlines"
f.seek(0, os.SEEK_SET)
print f.readlines()
print "tell", f.tell()

print 
print "test readlines(25)"
f.seek(0, os.SEEK_SET)
print f.readlines(25)
print "tell", f.tell()
print "linux ignore the 25"





