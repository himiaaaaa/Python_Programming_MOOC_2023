while True:
    word = input("Please type in a string: ")
    length = len(word)

    if word == "":
        break

    print(word)
    print(length * "-")


