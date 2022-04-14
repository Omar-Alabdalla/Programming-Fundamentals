import math
class Area:
    class Area:
        def Triangle(self, base, height):  # Finds the area of the Triangle

            area_of_triangle = (base * height) / 2
            return f"The area of your triangle is {area_of_triangle}"

        def Rectangle(self, width, length):  # Finds the area of the Rectangle
            area_of_rectangle = (width * length)
            return f"The area of your rectangle is {area_of_rectangle}"

        def Trapezoid(self, area, base, height):  # Finds the area of the Trapezoid
            area_of_trapezoid = ((area + base) / 2) * height
            return f"The area of your trapezoid is {area_of_trapezoid}"

        def Circle(self, radius):  # Finds the area of the Circle
            area_of_cricle = math.pi * (radius ** 2)
            return f"The area of your circle is {area_of_cricle}"