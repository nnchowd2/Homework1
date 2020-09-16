print("Birthday Calculator\nCurrent day")

month = int(input("Month: "))
day = int(input("Day: "))
year = int(input("Year: "))

print("Birthday")

month1 = int(input("Month: "))
day1 = int(input("Day: "))
year1 = int(input("Year: "))

if month1 == month and day1 == day:
    print("Happy Birthday!")
else:
    birth_day = year - year1 - ((month, day) < (month1, day1))
    print("You are", birth_day, "years old.")
