sentence = ""
pre_word = ""

while True:
    word = input("Please type in a word: ")

    if word == "end" or pre_word == word:
        break

    sentence += word + " "
    pre_word = word

print(sentence)