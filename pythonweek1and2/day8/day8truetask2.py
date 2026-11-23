numbers = [1, 2, 3, 4, 5]
k = int(input("Enter rotation steps (k): "))
k = k % len(numbers)  
k = k % len(numbers)  

numbers = numbers[-k:] + numbers[:-k]
print("List after rotation:", numbers)
