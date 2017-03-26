import datetime

print datetime.date.min
print datetime.date.max
print datetime.date.resolution

d1 = datetime.date(year=1, month=1, day=1)
print d1

today = datetime.date.today()
print today

d2 = datetime.date.fromtimestamp(1234567890)
print d2

print datetime.date.fromordinal(1)
print datetime.date.fromordinal(2)
print datetime.date.fromordinal(3)

del1 = datetime.timedelta(days=1, hours=2)
print d1
print d1 + del1

print d1.replace(month=3)

print d2.timetuple()
print d2.weekday()
print d2.isoweekday()
print d2.isocalendar()
print d2.isoformat()
print d2.ctime()
print d2.strftime("%Y:%d")

