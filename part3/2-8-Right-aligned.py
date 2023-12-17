word = input("Please type in a string: ")
length = len(word)
print_word = ""
n = 0

if length <= 20:
    print((20 - length) * "*" + word)
else:
    while n < 20:
        print_word += word[n]
        n += 1
    print(print_word)