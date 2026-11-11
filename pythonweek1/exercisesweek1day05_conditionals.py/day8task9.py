home = int(input("Enter home team goals: "))
away = int(input("Enter away team goals: "))
if home < 0 or away < 0:
    print("Invalid goals!")
else:
    if home > away:
        print("Home team wins!")
    elif home < away:
        print("Away team wins!")
    else:
        print("It's a draw!")