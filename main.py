import math

class Point:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, other):
		return Point(self.x + other.x, self.x + other.y)

	def distance(self, other):
		return math.sqrt((self.x - other.x)**2 + (self.y + other.y)**2)



p1 = Point (1, 1)
p2 = Point (2, 2)
p3 = p1 +p2
print(p3.x, p3.y)
s = p1.distance(p2)
print("Distance is", s)