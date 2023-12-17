limit = int(input("Limit: "))
sum = 0
next_num = 1
list = []
sentence = ""

while sum < limit:
    sum += next_num
    list.append(str(next_num))
    next_num += 1

sentence = " + ".join(list)

print(f"The consecutive sum: {sentence} = {sum}")