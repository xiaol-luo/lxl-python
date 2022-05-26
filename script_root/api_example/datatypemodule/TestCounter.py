import collections

cnt = collections.Counter()
print cnt

print collections.Counter(cats=4, dogs=3)

fruitList = ["apple", "orange", "banana", "banana"]
fruitListCnt = collections.Counter(fruitList)
print fruitListCnt

fruitDict = { "apple":3, "orange": 4, "banana":2, "juice":-1 }
fruitDictCnt = collections.Counter(fruitDict)
print fruitDictCnt

print "fruitListCnt[apple]", fruitListCnt["apple"]
print "fruitListCnt[cat]", fruitListCnt["cat"]

print list(fruitDictCnt.elements())
print fruitDictCnt.most_common(2)

fruitDictCnt += collections.Counter()
print "fruitDictCnt += collections.Counter()", fruitDictCnt 

print "fruitDictCnt + fruitListCnt", fruitDictCnt + fruitListCnt
print "fruitDictCnt - fruitListCnt", fruitDictCnt - fruitListCnt
print "fruitDictCnt & fruitListCnt", fruitDictCnt & fruitListCnt
print "fruitDictCnt | fruitListCnt", fruitDictCnt | fruitListCnt

fruitListCnt.update(fruitDict)
print fruitListCnt

fruitDictCnt.update(fruitList)
print fruitDictCnt

print sum(fruitDict.values())

