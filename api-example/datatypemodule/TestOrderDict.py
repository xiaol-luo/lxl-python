import collections

tmpDict = { "banan":2, "apple" : 1, "orange":2 }

orDict = collections.OrderedDict(sorted(tmpDict.items(), key=lambda t: t[0]))
print orDict

orDict = collections.OrderedDict(sorted(tmpDict.items(), key=lambda t: t[1]))
print orDict

orDict.popitem()
print orDict

orDict.popitem(False)
print orDict

def sortedCmp(x, y):
	if (x[1] == y[1]):
		return 0
	return x[1] < y[1] and -1 or 1

print sorted(tmpDict.items(), cmp=sortedCmp, key= lambda t: t)