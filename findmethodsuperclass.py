
class Triangle:

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def find_area(self):
        print((self.base * self.height) / 2)


class RightTriangle(Triangle):

    def display_area(self):
        print("=== Right Triangle Area ===")

        # This line calls the method from the Triangle class
        Triangle.find_area(self)  # You could also use super().find_area()

right_triangle = RightTriangle(5, 6)
right_triangle.display_area()