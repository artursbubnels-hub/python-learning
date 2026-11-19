numbers = [10, 45, 23, 89, 45, 67, 89, 12]
       
largest = second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
    

print("Largest:", largest)
print("Second largest:",second_largest)