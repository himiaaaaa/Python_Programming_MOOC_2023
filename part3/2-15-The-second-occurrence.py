string = input("Please type in a string: ")
substring = input("Please type in a substring: ")
length = len(substring)

index = string.find(substring)

if index != -1:
    index = string.find(substring, index + length)

    if index == -1:
        print("The substring does not occur twice in the string.")
    else:
        print(f"The second occurrence of the substring is at index {index}.")
else:
    print("The substring does not occur twice in the string.")