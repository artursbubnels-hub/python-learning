shopping_ammount = int(input("Enter the shopping amount: "))
vip = input("Are you a VIP customer? (yes or no): ").strip().lower()
coupon = input("Do you have a coupon? (yes or no): ").strip().lower()

if shopping_ammount >= 200:
    discount = 0.20
elif shopping_ammount < 200:
    discount = 0.10

    if vip == "yes":
        discount += 0.05
    if coupon == "yes":
        discount += 0.05
final_price = shopping_ammount - (shopping_ammount * discount)

print("initial ammount", shopping_ammount ,"Total discount:", discount * 100, "%" "Final price:", final_price)
