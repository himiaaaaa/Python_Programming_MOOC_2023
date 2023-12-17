word_1 = input("Please type in string 1: ")
word_2 = input("Please type in string 2: ")

len_1 = len(word_1)
len_2 = len(word_2)

if len_1 > len_2:
    print(f"{word_1} is longer")
elif len_1 < len_2:
    print(f"{word_2} is longer")
else:
    print("The strings are equally long")