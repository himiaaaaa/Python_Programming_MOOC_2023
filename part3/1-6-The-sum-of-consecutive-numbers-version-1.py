limit = int(input("Limit: "))
sum = 0
next_num = 1

while sum < limit:
    sum += next_num
    next_num += 1

print(sum)