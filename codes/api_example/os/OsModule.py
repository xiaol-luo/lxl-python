import os
import stat

print os.name

print
print os.environ['LANG']

print
print os.getcwd() 

currDir = os.getcwd()
print os.access(currDir, os.F_OK)
print os.access(currDir, os.R_OK)
print os.access(currDir, os.W_OK)
print os.access(currDir, os.X_OK)

os.chdir("../")
print os.getcwd()
os.chdir(currDir)
print os.getcwd()

print os.chmod("OsModule.py", stat.S_IRWXO | stat.S_IRWXU | stat.S_IRWXG) 

#os.chroot("../")
#print os.getcwd()

print os.listdir(os.path.dirname(os.path.abspath(".")))

print os.system("ls")

print os.times()

print os.curdir
