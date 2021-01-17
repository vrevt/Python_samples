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


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 *self.base* self.height


class RightPyramid(Triangle, Square):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 *perimeter* self.slant_height + base_area



cube = Cube(3)
print(cube.surface_area())
pyramid = RightPyramid(2, 4)

# using mro - method resolution order.
print(RightPyramid.__mro__)

