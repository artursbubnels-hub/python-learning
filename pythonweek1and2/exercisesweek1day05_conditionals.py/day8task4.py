time = int(input("Enter the time of the day "))
while time < 0 or time > 24:
    print("give me a correct time date ")
    time = int(input("Enter the time of the day "))
if time < 5:
    print("Good night!")
elif time < 12:
    print("Good morning!")
elif time < 17:
    print("Good afternoon!")
elif time < 21:
    print("Good evening!")
else:
    print("Good night!")
