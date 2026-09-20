# Here is a function that calculates the average of a list of grades.
def calculate_average(grades):
    return sum(grades) / len(grades)

# Here is a list of student grades.
grades = [85, 90, 78, 95, 88]

# Here is the returned value stored in a variable.
average_grade = calculate_average(grades)
print("Average grade:", average_grade)
