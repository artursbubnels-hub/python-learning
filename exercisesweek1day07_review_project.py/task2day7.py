print("Bill split calculator")
num_people = float(input("Ammount of people "))
bill_ammount = int(input("The toal bill "))
tip_percent = float(input("Tip percent "))

while num_people < 1:
    print("Please enter at least 1 person.")
    num_people = int(input("How many people are splitting the bill? "))

tip_ammount =(tip_percent / 100) * bill_ammount
grand_total = bill_ammount + tip_ammount
per_person = grand_total / num_people

print(f"tip: {tip_ammount:.2f}")
print(f"grand total: {grand_total:.2f}")
print(f"Ammount per person: {per_person:.2f}")

if per_person <= 50:
    print("Expensiv evening.")