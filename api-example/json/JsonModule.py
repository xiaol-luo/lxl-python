#coding=utf-8
import os
import json
import codecs

jsonObj = {"name":u"罗晓龙", "phone":15818806411, "strList":["hello", "world", u"你好"]}

filePath = "data.txt"
if not os.path.exists(filePath):
	with open(filePath, "w") as f:
		pass

with codecs.open(filePath, "w", encoding="UTF-8") as f:
	json.dump(jsonObj, f, ensure_ascii=False)

with codecs.open(filePath, "r", encoding="UTF-8") as f:
	print json.load(f, encoding="UTF-8")

print "---------------------------------"
print json.dumps(jsonObj, ensure_ascii=False)

print "---------------------------------"
jsonStr = '{"name":"罗小龙", "phone":15818806411, "strList":["hello","world"]}'
print json.loads(jsonStr, encoding='utf-8')


class Item:
	TYPE = "Item"
	def __init__(self):
		self.aa = ""
		self.bb = ""


item = Item()
item.aa = "aa"
item.bb = "bb"

print "---------- use dumps default --------------------"
#default transfer input obj to base type which json can handle
def ItemDefault(obj):
	if isinstance(obj, Item):
		return { "ObjectType":Item.TYPE, "Item-aa": obj.aa, "Item-bb": obj.bb }
	return obj

print json.dumps(item, default=ItemDefault)
print json.dumps([item, 1, 2, 3], default=ItemDefault)

print "---------------- use load object_hook ------------"
def ItemHook(objDict):
	if (objDict['ObjectType'] == Item.TYPE):
		item = Item()
		item.aa = objDict.get("Item-aa", "")
		item.bb = objDict.get("item-bb", "")
		return item
	return objDict

print json.loads('{"Item-bb": "bb", "Item-aa": "aa", "ObjectType": "Item"}', object_hook=ItemHook)
print json.loads('[{"Item-bb": "bb", "Item-aa": "aa", "ObjectType": "Item"}, 1, 2, 3]', object_hook=ItemHook)


class ItemEncoder(json.JSONEncoder):
	def default(self, o):
		return ItemDefault(o)

class ItemDecoder(json.JSONDecoder):
	def __init__(self, encoding):
		json.JSONDecoder.__init__(self, encoding)
		self.object_hook = ItemHook

print "--------------- use cls  ---------------------"
print json.dumps([item, 1, 2, 3], cls=ItemEncoder)
print json.loads('[{"Item-bb": "bb", "Item-aa": "aa", "ObjectType": "Item"}, 1, 2, 3]', cls=ItemDecoder)