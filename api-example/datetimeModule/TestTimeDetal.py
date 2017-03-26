import datetime

print datetime.timedelta.min
print datetime.timedelta.max
print datetime.timedelta.resolution

d1 = datetime.timedelta(days=1, seconds=1, microseconds=1,
		milliseconds=2, minutes=1, hours=1, weeks=1)
print d1

d2 = datetime.timedelta(days=2, seconds=2, microseconds=2,
		milliseconds=2, minutes=2, hours=2, weeks=2)
print d2

print "d1 + d2 = ", d1 + d2	
print "d1 - d2 = ", d1 - d2	
print "d1 * 3 = ", d1 * 3
print "+d1", +d1
print "-d1", -d1
print "abs(d1)", abs(d1)
print "abs(-d1)", abs(-d1)

print "d1.total_seconds()", d1.total_seconds()
