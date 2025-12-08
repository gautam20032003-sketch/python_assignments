year = int(input("Enter a year: "))

if (year % 400 == 0):
    print(year, " leap year.")
elif (year % 100 == 0):
    print(year, " not leap year.")
elif (year % 4 == 0):
    print(year, "leap year.")
else:
    print(year, " not leap year."
