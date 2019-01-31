# namedtuples

# when the classes are very simple, we can create very simple classes
# using nametuple


from collections import namedtuple

# define Point class
Point = namedtuple('Point', ['x', 'y'])

point1 = Point(1, 2)
print(point1.x) # 1


Point3d = namedtuple('Point3', ['x', 'y', 'z'])

point2 = Point3d(23, 34, 21)
print(point2.z) # 21

