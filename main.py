def calculate_average(grades_list):
    if not grades_list:
        return 0.0
    total_sum = sum(grades_list)
    grades_count = len(grades_list)
    return total_sum / grades_count

def find_highest(grades_list):
    if not grades_list:
        return None
    highest_value = max(grades_list)
    return highest_value

def filter_passed(students_data):
    passed_students = []
    for student_name, student_grade in students_data.items():
        if student_grade >= 60:
            passed_students.append(student_name)
    return passed_students

def main():
    students_data = {
        "Алиса": 85,
        "Борис": 45,
        "Виктор": 72,
        "Галина": 90,
        "Дмитрий": 58
    }
    
    grades_list = list(students_data.values())
    
    average_grade = calculate_average(grades_list)
    highest_value = find_highest(grades_list)
    passed_students = filter_passed(students_data)
    
    print(f"Средний балл: {average_grade:.2f}")
    print(f"Высший балл: {highest_value}")
    print(f"Сдали экзамен: {', '.join(passed_students)}")

if __name__ == "__main__":
    main()