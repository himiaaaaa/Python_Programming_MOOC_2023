word = input("Please type in a string: ")
length = len(word)
n = length - 1
while n >= 0:
    print(word[n:length])
    n -= 1