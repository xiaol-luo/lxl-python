#!/usr/bin/python
#func.py

def printMax(a, b):
    if a > b:
        print("printMax: %d is maxinum" %a)
    else:
        print("printMax: %d is maxinum" %b)

printMax(3, 4)

def defaultParam(a, b = 3):
    if (a > b):
        print("defaultParam: %d is maxinum" %a)
    else:
        print("defaultParam: %d is maxinum" %b)

defaultParam(5)

def keyParam(a, b=3, c=4):
    print("a:%d, b:%d, c:%d" %(a, b, c))

keyParam(1, c=2)
keyParam(1, b=1)
keyParam(a=1, b=2, c=3)

def globalFun():
    global g_param
    print("g_param is %d" %g_param)
    g_param = 2

g_param = 30
globalFun()
print("excute globalFun g_param is %d" %g_param)

def returnFun():
    return 123

return_val = returnFun()
print("return value is %d" %return_val)
