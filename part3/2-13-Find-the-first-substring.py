word = input("Please type in a word: ")
character = input("Please type in a character: ")
length = len(word)

index = word.find(character)

if index + 2 >= len(word) or index == -1:
    print("")
else:
    print(word[index:index+3])
