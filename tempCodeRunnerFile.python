numbers = (1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 5)
result = []
if numbers:
    current_num = numbers[0]
    count = 1

    for num in numbers[1:]:
        if num == current_num:
            count += 1
        else:
            result.append((current_num, count))
            current_num = num
            count = 1

    result.append((current_num, count))

result = tuple(result)
print(result)