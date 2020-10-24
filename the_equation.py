import math
def solve_equation(a, b, c):
    D = b ** 2 - 4 * a * c
    if D > 0:
        print("два корня")
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print("x1=", x1, "x2=", x2)
    elif D == 0:
        print("один корень")
        x = -b / (2 * a)
        print("x=", x)
    elif D < 0:
        print("нет корней")


a = int(input())
b = int(input())
c = int(input())
solve_equation(a, b, c)
