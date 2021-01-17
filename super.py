class Rectangle:
	def __init__(self, length, width):
		self.length = length
		self.width = width

	def area(self):
		return self.length * self.width


class Square(Rectangle):
	def __init__(self, length):
		super().__init__(length, length)


class Cube(Square):
	def surface_area(self):
		face_area = super().area()
		return face_area * 6

	def volume(self):
		face_area = super().area()
		return face_area * self.length


cube = Cube(3)
print(cube.surface_area())
