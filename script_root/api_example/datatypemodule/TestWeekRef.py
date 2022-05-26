import collections
import weakref
import datetime
import time

#Item = collections.namedtuple("Item", "x, y")
class Item():
	def __init__(self):
		self.x = 1
		self.y = 2

def PrintCollect(item):
	print "PrintCollect ", datetime.datetime.now()

item = Item()
print item

wrItem = weakref.ref(item, PrintCollect)
print wrItem

wpItem = weakref.proxy(item, PrintCollect)
print wpItem

print wrItem().x

print wpItem.x

print weakref.getweakrefcount(item)
print weakref.getweakrefs(item)

wValueDict = weakref.WeakValueDictionary()
wValueDict["1024"] = item

mKeyDict = weakref.WeakKeyDictionary()
mKeyDict[item] = "1024"

#this value is handle item, should set None
for key, value in list(wValueDict.items()):
	print key, value

#this value is handle item, should set None
for key, value in list(mKeyDict.items()): 
	print key, value

key = None 
value = None 

item = None
time.sleep(1)
print "------ sleep -------------"

item = wrItem()
if item:
	print item.x

#if wpItem:  # this will fail. weakproxy has no way to test if item had been recycled
#	print wpItem.x
item = wValueDict.get("1024")
print item

#this value is handle item, should set None
for key, value in list(wValueDict.items()):
	print key, value

#this value is handle item, should set None
for key, value in list(mKeyDict.items()): 
	print key, value


