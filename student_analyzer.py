# ====================================================
# Python Implementation of Student Performance Analyzer
# Direct translation of the algorithm from Task 1-c
# ====================================================

# Sample student data for demonstration
students = [
    {"id": 1, "grades": [60, 70]},  # Test Case 1: Good grades
    {"id": 2, "grades": [40, 45]},  # Test Case 2: Weak grades
    {"id": 3, "grades": []}         # Test Case 3: No grades
]

print("Student Performance Analysis Results:")
print("=" * 50)

# Process each student according to the algorithm
for student in students:
    # Initialize variables as per algorithm
    sum_grades = 0
    count = 0
    weak_modules = []
    
    # Loop through each grade (implements the FOR loop requirement)
    for grade in student["grades"]:
        sum_grades += grade      # sum = sum + g
        count += 1               # count = count + 1
        
        # If-else statement for weak grade detection
        if grade < 50:           # if g < 50:
            weak_modules.append(grade)  # weak.append(g)
    
    # Calculate average with edge case handling
    if count > 0:                # if count > 0:
        average = sum_grades / count  # average = sum / count
    else:                        # else:
        average = 0              # average = 0
    
    # Determine student status with if-else
    if average < 50:             # if average < 50:
        status = "At Risk"       # status = "At Risk"
    else:                        # else:
        status = "OK"            # status = "OK"
    
    # Output results
    print(f"\nStudent {student['id']}:")
    print(f"  Grades: {student['grades']}")
    print(f"  Average Score: {average:.2f}")
    print(f"  Weak Modules: {weak_modules}")
    print(f"  Status: {status}")

print("\n" + "=" * 50)
print("Algorithm execution completed successfully.")
