word = input("Please type in a string: ")
amount = int(input("Please type in an amount: "))
n = 1
sentence = ""

while n <= amount:
    sentence += word
    n += 1

print(sentence)