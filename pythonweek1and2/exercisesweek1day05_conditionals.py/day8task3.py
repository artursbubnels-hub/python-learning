weight = int(input("how much does the cargo weigh?" ))
express = input("is express shipping required? (yes/no) ").lower()
if weight < 1 or weight == 0:
    print("Invalid weight, Please give me a positive number")
else:
    if weight >= 1:
        price = 5
    elif weight < 5:
        price = 10
    else:
        price = 20
    if express == "yes":
        price += 7  
    print(f"The weight of the cargois: ${price:.2f}")