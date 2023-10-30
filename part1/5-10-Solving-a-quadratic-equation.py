from math import sqrt

a = float(input("Value of a: "))
b = float(input("Value of b: "))
c = float(input("Value of c: "))

print(f"The roots are {(-b + sqrt(b ** 2 -4 * a * c))/(2 * a)} and {(-b - sqrt(b ** 2 -4 * a * c))/(2 * a)}")