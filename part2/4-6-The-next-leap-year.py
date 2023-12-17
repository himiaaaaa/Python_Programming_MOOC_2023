year = int(input("Year: "))
original_year = year

while True:
    year += 1

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        break

print(f"The next leap year after {original_year} is {year}")


