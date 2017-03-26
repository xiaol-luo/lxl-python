import bisect

class Item():
	def __init__(self):
		self.aa = 0
		self.bb = 0

tmpList = [1, 7, 5, 15]
tmpList = sorted(tmpList, key=lambda x: x)
print tmpList

print "bisect_left", bisect.bisect_left(tmpList, 1, 0, len(tmpList))
print "bisect_right", bisect.bisect_right(tmpList, 1)

print "insort_left", bisect.insort_left(tmpList, 7)
print tmpList

print "insort_right", bisect.insort_right(tmpList, 7)
print tmpList

tmpSet = set(tmpList)
print tmpSet