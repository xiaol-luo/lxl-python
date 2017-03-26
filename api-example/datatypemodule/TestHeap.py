import heapq

tl = [10, 9, 2, 4, 5, 3, 4]

print heapq.heapify(tl)
print tl

print "push", heapq.heappush(tl, 100)
print tl

print "pop", heapq.heappop(tl)
print tl

print "pushpop", heapq.heappushpop(tl, 1)
print tl

print "replace", heapq.heapreplace(tl, 0)
print tl

print "n-largest", heapq.nlargest(3, [3, 2, 77, 28, 55, 1])

print "n-nsmallest", heapq.nsmallest(3, [3, 2, 77, 28, 55, 1])

l1 = [1, 7, 5]
l2 = [2, 6, 4]
hIter = heapq.merge(l1, l2)
for item in hIter:
	print item


