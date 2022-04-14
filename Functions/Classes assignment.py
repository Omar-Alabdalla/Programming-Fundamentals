# Function are created by doing def functionname(params):
# For python instead of curly brackets you make what you want your functions to do indented after the function is defined.
# Classes are created in a similar way as functions except its class className:
# It works the same way except for instead of what you want the class do to you add functions underneath.
# they are called by doing className.functionName(parameters) and the parameter variables don't need to be the same name as what they are in the defined function.

import math


class Area:  # Area commands

    def Triangle(self, base, height):  # Finds the area of the Triangle
        area_of_triangle = (base * height) / 2
        return f"The area of your triangle is {area_of_triangle}"

    def Rectangle(self, width, lenggth):  # Finds the area of the Rectangle
        area_of_rectangle = (width * lenggth)
        return f"The area of your rectangle is {area_of_rectangle}"

    def Trapezoid(self, area, base, height):  # Finds the area of the Trapezoid
        area_of_trapezoid = ((area + base) / 2) * height
        return f"The area of your trapezoid is {area_of_trapezoid}"

    def Circle(self, radius):  # Finds the area of the Circle
        area_of_cricle = math.pi * (radius ** 2)
        return f"The area of your circle is {area_of_cricle}"


class Help:  # Help commands
    def Help(self):
        return 'Triangle, Rectangle, Trapezoid, and Circle. \nYou can also input Quit to stop the program'

    def HelpRectangle(self):
        return "This returns the area of a rectangle"

    def HelpTriangle(self):
        return "This returns the area of a triangle"

    def HelpTrapezoid(self):
        return "This returns the area of a trapezoid"

    def HelpCircle(self):
        return "This returns the area of a circle"


userChoice = str(0)
leaveMessage = "Quit"
while userChoice.lower() != leaveMessage.lower():
    userChoice = str(input("Enter help to receive a help command! "))
    if userChoice.lower() == "help":
        print(
            f"There are help commands for each of the following: {Help.Help(Help())} to reach these commands just input help followed by the shape.")

    elif userChoice.lower() == "help rectangle":
        print(f"{Help.HelpRectangle(Help())}")

    elif userChoice.lower() == "help triangle":
        print(f"{Help.HelpTriangle(Help())}")

    elif userChoice.lower() == "help trapezoid":
        print(f"{Help.HelpTrapezoid(Help())}")

    elif userChoice.lower() == "help circle":
        print(f"{Help.HelpCircle(Help())}")

    elif userChoice.lower() == "circle":
        rad = int(input("Please input the radius of your circle "))
        print(Area.Circle(Area(), rad))

    elif userChoice.lower() == "triangle":
        bas = int(input("Please input the base of your triangle "))
        h = int(input("Please input the height of your triangle "))
        print(Area.Triangle(Area(), bas, h))

    elif userChoice.lower() == "rectangle":
        w = int(input("Please input the width of your rectangle "))
        length = int(input("please input the length of your rectangle "))
        print(Area.Rectangle(Area(), w, length))

    elif userChoice.lower() == "trapezoid":
        a = int(input("Please input the first base of your trapezoid "))
        b = int(input("Please input the second base of your trapezoid "))
        h = int(input("Please input the height of your trapezoid "))
        print(Area.Trapezoid(Area(), a, b, h))
    else:  # Tells users they had a typo
        print("Your input didn't work try the help command to see all the commands.")
