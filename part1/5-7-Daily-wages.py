hourly_wage = float(input("Hourly wage: "))
hour = float(input("Hours worked: "))
day = input("Day of the week: ")

if day == "Sunday":
    print(f"Daily wages: {hourly_wage * hour * 2} euros")

if day != "Sunday":
    print(f"Daily wages: {hourly_wage * hour} euros")