F = int(input("Please type in a temperature (F): "))
C = (F - 32) / 1.80

if C < 0:
    print(f"{F} degrees Fahrenheit equals {C} degrees Celsius")
    print("Brr! It's cold in here!")

if C >= 0:
    print(f"{F} degrees Fahrenheit equals {C} degrees Celsius")