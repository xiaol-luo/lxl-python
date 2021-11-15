import collections

tmpList = [("yellow", 1), ("blue", 2), ("blue", 3)]

#the value is auto construct when the key insert
dd = collections.defaultdict(list)

for color, cnt in tmpList:
	dd[color].append(cnt)

print dd 
