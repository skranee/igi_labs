from circle import area
from square import perimeter

r = 5
a = 3


def sum(a, b):
    return area(a) + perimeter(b)


print("Sum =", sum(r, a))
