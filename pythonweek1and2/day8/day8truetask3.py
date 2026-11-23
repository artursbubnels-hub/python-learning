numbers = [1, 2, 3, 4, 5, 6, 7]
target = 10
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i != j and numbers[i] + numbers[j] == target:
            print(f"{numbers[i]} + {numbers[j]} = {target}")