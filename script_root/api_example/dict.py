#!/usr/bin/python
#dict.py

kName = "name"
vName = "luoxiaolong"

kPhone = "phone"
vPhone = "15818806411"

kMail = "mail"
vMail = "823121828@qq.com"

userDict = {}

print "len", len(userDict)

userDict[kName] = vName
print userDict

del userDict[kName]
print userDict

print "key in dict", kName in userDict
print "key in dict", kName not in userDict

userDict[kName] = vName
print userDict
tmpDict = userDict.copy()
userDict.clear()
print "clear", userDict
print "tmpDict", tmpDict

userDict[kName] = vName
userDict[kPhone] = vPhone
userDict[kMail] = vMail
print "has_key kPhone", userDict.has_key(kPhone)
print "get kName who", userDict.get(kName, "who")
print "get xx who", userDict.get("xx", "who")
print "items", userDict.items()

for (key, val) in userDict.iteritems():
	print "iteritems:", key, val

for key in userDict.iterkeys():
	print "iterkeys", key

for val in userDict.itervalues():
	print "itervalues", val

print "keys", userDict.keys()
print "values", userDict.values()

item = userDict.popitem()
print "popitem", item, userDict

val = userDict.pop(kName, "who")
print "pop kName", val, userDict

userDict.update(tmpDict)
print "tmpDict", tmpDict
print userDict
