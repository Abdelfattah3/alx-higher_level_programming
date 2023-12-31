#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

try:
    mysquare = Rectangle.square(-2)
    print("{} / {}".format(mysquare.width, mysquare.height)) 
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    mysquare = Rectangle.square("12")
    print("{} / {}".format(mysquare.width, mysquare.height)) 
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

my_square = Rectangle.square(2)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)
