word = input("Please type in a word: ")
character = input("Please type in a character: ")
length = len(word)

index = word.find(character)

while index != -1 and index + 2 < length:
    print(word[index:index+3])
    index = word.find(character, index + 1)