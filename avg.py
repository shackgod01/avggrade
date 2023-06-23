def calculate_average_grade(grades):
    total_grades = len(grades)
    if total_grades == 0:
        return 0

    grade_sum = sum(grades)
    average_grade = grade_sum / total_grades
    return average_grade


course_grades = [85, 90, 92, 78, 88]
average = calculate_average_grade(course_grades)
print(f"Average grade: {average}")
