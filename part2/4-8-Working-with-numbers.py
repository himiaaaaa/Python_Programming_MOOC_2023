print("Please type in integer numbers. Type in 0 to finish.")
length = 0
sum = 0
positive = 0
negative = 0

while True:
    number = int(input("Number: "))

    if number == 0:
        break

    length += 1
    sum += number

    if number < 0:
        negative += 1
    elif number > 0:
        positive += 1


print(f"Numbers typed in {length}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {sum/length}")
print(f"Positive numbers {positive}")
print(f"Negative numbers {negative}")