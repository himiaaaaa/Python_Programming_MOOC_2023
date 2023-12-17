word = input("Word: ")
length = len(word)
print(30 * "*")
space_len = 15 - length//2 - 1
space = " " * space_len
space_left = " " * (space_len - 1)

if length%2 != 0:
    print(f"*{space}{word}{space_left}*")
else:
    print(f"*{space}{word}{space}*")
print(30 * "*")