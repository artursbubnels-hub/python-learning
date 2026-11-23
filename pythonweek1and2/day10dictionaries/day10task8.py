grades = {
    "Alex": 85,
    "John": 92,
    "Sarah": 78,
    "Mike": 35
}
average = sum(grades.values()) / len(grades)


highest = max(grades.values())
lowest = min(grades.values())

print("Average grade:", average)
print("Highest grade:", highest)
print("Lowest grade:", lowest)

print("Students who scored above 80:")
for student, grade in grades.items():
    if grade > 80:
        print(student, grade)