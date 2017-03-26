#/usr/bin/python
#lists.py

apple = "apple"
banana = "banana"
orange = "orange"

tmpList = [apple, banana, orange]
shopList = [apple, banana]
print shopList
print "len", len(shopList)

shopList[0] = orange 
print shopList
shopList[0:2] = tmpList
print shopList

shopList[2:] = tmpList
print shopList

del shopList[0]
print shopList
del shopList[0:-1:2]
print shopList

shopList.append(apple)
print shopList

shopList.extend(tmpList)
print shopList

print "count", shopList.count(apple)
print "index", shopList.index(orange)

shopList.insert(0, banana)
print "insert 0 banana", shopList

ret = shopList.pop()
print "pop ", ret, shopList

shopList.remove(apple)
print "remove apple", shopList

shopList.reverse()
print "reverse", shopList

del shopList[0]
print "del shopList[0]", shopList

shopList.sort()
print "sort", shopList
