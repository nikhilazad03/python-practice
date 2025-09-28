# Manage student grades using dictionary
students = {
    "Alice": [85, 92, 78],
    "Bob": [79, 81, 86],
    "Charlie": [92, 88, 95]
}

# Calculate average grade for each student
for student, grades in students.items():
    avg = sum(grades) / len(grades)
    print(f"{student}: Average Grade = {avg:.2f}")

# Add a new student
students["David"] = [90, 87, 93]
print("\nUpdated Students:", students)
