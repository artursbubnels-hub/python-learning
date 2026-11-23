day= int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))
print(f"{day}/{month}/{year}")
if (day >= 1 and day <31 and month >= 1 and month <= 12 and year >= 1 and year <= 10000):
    print("The date is valid.")
else:
    print("The date is invalid.")