salary = int(input("Enter your salary: "))
experience = int(input("Enter your years of experience: "))
debt = int(input("Enter your total debt: "))




if salary >= 1500 and experience >= 2 and debt < salary * 0.4:
    print("You are eligible for a loan.")
else:
    print("Loan not approved. The following requirements were not met:")

    if salary < 1500:
        print("- Your salary must be at least 1500.")

    if experience < 2:
        print("- You must have at least 2 years of experience.")

    if debt >= salary * 0.4:
        print("- Your debt must be less than 40% of your salary.")