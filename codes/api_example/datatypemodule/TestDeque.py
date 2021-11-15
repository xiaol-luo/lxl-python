import collections

apple = "apple"
banana = "banana"
cat = "cat"
orange = "orange"

deq = collections.deque([apple, banana])
print deq

deq.append(cat)
print "append", deq

deq.appendleft(orange)
print "appendleft", deq

print "count", deq.count(apple)

deq.extend([apple, banana])
print "extend", deq

deq.extendleft([apple, banana])
print "extendleft", deq

elem = deq.pop()
print "pop", deq, "elem", elem

elem = deq.popleft()
print "popleft", deq, "elem", elem

deq.remove(apple)
print "remove(apple)", deq

deq.reverse()
print "reverse", deq

deq.rotate(1)
print "rotate", deq

print "maxlen", deq.maxlen




