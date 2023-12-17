word = input("Please type in a string: ")
length = len(word) - 1

second = word[1]
second_to_last = word[length - 1]

if second == second_to_last:
    print(f"The second and the second to last characters are {second}")
else:
    print(f"The second and the second to last characters are different")