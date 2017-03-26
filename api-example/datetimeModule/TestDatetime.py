import datetime

print datetime.datetime.min
print datetime.datetime.max
print datetime.datetime.resolution

print datetime.datetime.today()
print datetime.datetime.now()
print datetime.datetime.utcnow()
print datetime.datetime.fromtimestamp(1234)
print datetime.datetime.utcfromtimestamp(1234)

t1 = datetime.time(hour=1, minute=1, second=1, microsecond=1, tzinfo=None)
print t1

print datetime.time.time()