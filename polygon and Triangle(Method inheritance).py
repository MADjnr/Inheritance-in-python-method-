class Polygon:

    def __init__(self, num_sides, color):
        self.num_sides = num_sides
        self.color = color

    def describe_polygon(self):
        print(f"This polygon has {self.num_sides} sides and its color is {self.color}")


class Triangle(Polygon):

    NUM_SIDES = 3

    def __init__(self, base, height, color):
        Polygon.__init__(self, Triangle.NUM_SIDES, color)
        self.base = base
        self.height = height

    def find_area(self):
        return(self.base * self.height) / 2


class Square(Polygon):

    NUM_SIDES  = 4

    def __init__(self, side_length, color):
        Polygon.__init__(self, Square.NUM_SIDES, color)
        self.side_length = side_length

    def find_area(self):
        return self.side_length ** 2


my_triangle = Triangle(10, 2, 'Yellow')
print(my_triangle.num_sides)
my_triangle.describe_polygon()
print(my_triangle.find_area())


my_square = Square(12, 'Brown')
my_square.describe_polygon()
square_area = my_square.find_area()
print(square_area)