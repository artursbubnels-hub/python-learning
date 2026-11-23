numbers = (1, 2, 3, 2, 4, 5, 3, 6, 1, 7)
seen = set()
duplicates = set()

for item in numbers:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)

print(list(duplicates))