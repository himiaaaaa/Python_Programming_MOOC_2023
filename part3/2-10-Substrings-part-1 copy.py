word = input("Please type in a string: ")
length = len(word)
n = 0
print(word[0])
while n+2 <= length:
    print(word[0:n+2])
    n += 1