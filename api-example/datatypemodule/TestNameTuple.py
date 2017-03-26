import collections

Point = collections.namedtuple("Point", "x, y", verbose=False)
Point = collections.namedtuple("Point", "x y", verbose=False)
Point = collections.namedtuple("Point", ["x", "y"], verbose=False)

p = Point(1, y=2)
print p
print p[0], p[1]
print p.x, p.y

p = Point._make([11, 22])
#p = Point._make([11, 22, 33])
print p

print p._asdict()

p._replace(y=33)
print p

print p._fields

print getattr(p, 'x')

class PointClass(collections.namedtuple('PointClass', 'x, y')):
	def __str__(self):
		return "PointClass x={0.x:f}, y={0.y:f}".format(self)

pc = PointClass(111, 222)
print pc

#use as enmu
EnumStateList = (
	"Open",
	"Close",
	"Pending"
	)
EnumState = collections.namedtuple("EnumState", EnumStateList)._make(range(len(EnumStateList)))
print EnumState