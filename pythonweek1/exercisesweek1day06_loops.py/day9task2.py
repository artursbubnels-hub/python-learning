n = int(input("Give me a number: "))

if n < 2:
    print("There are no prime numbers.")
else:
    print(f"Prime numbers between 2 and {n}:")

    for num in range(2, n + 1):
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                break
        else:
            print(num, end=" ")