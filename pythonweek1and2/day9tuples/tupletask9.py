students = (
    ("John", 85, 90, 88),
    ("Sarah", 92, 95, 89),
    ("Mike", 78, 82, 80),
    ("Emma", 90, 91, 94)
)

top_student = ""
highest_avg = 0
total_sum = 0
total_count = 0

for student in students:

    name = student[0]
    grades = student[1:]
    
    avg = sum(grades) / len(grades)
    print(f"{name}: {avg:.2f}")
    
    if avg > highest_avg:
        highest_avg = avg
        top_student = name
        
    total_sum += sum(grades)
    total_count += len(grades)

overall_avg = total_sum / total_count

print(f"\nTop student: {top_student}")
print(f"Overall average: {overall_avg:.2f}")