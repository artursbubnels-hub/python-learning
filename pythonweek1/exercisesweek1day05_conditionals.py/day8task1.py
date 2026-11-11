age = int(input("How old are you?" ))
student = input("Are you a student? (yes/no) ").lower()
if age < 6:
    price = 0
elif age < 17:
    price = 5
elif age < 65:
    price = 10
else:
    price = 6
if student == "yes":
    price *= 0.8  
print(f"The ticket price is: ${price:.2f}")