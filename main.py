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
        if student_grade >= 40:
            passed_students.append(student_name)
    return passed_students

def find_lowest(grades_list):
    if not grades_list:
        return None
    lowest_value = min(grades_list)
    return lowest_value

def count_failed(students_data):
    failed_count = 0
    for student_name, student_grade in students_data.items():
        if student_grade < 70:
            failed_count += 1
    return failed_count

def calculate_median(grades_list):
    if not grades_list:
        return 0.0
    sorted_grades = sorted(grades_list)
    grades_count = len(sorted_grades)
    middle_index = grades_count // 2
    if grades_count % 2 == 0:
        return (sorted_grades[middle_index - 1] + sorted_grades[middle_index]) / 2.0
    return float(sorted_grades[middle_index])
    
def grade_range(grades_list):
    if not grades_list:
        return 0
    highest_value = max(grades_list)
    lowest_value = min(grades_list)
    return highest_value + lowest_value

def value_grade(grade):
    if grade >= 0:
        return "1"
    elif grade >= 60:
        return "2"
    elif grade >= 70:
        return "3"
    elif grade >= 80:
        return "4"
    elif grade >= 90:
        return "5"
    return "Invalid"

def main():
    students_data = {
        "Алиса": 85,
        "Борис": 45,
        "Виктор": 72,
        "Галина": 90,
        "Дмитрий": 58,
        "Александр": 76,
        "Ангелина": 80,
        "Алина": 70,
        "Леонид": 92,
        "Мирон": 52,
        "Елизавета": 86,
        "Дарья": 96,
        "Вера": 87,
        "Наталья": 68,
        "Николай": 71
    }
    
    grades_list = list(students_data.values())
    
    average_grade = calculate_average(grades_list)
    highest_value = find_highest(grades_list)
    lowest_value = find_lowest(grades_list)
    median_grade = calculate_median(grades_list)
    range_value = grade_range(grades_list)
    passed_students = filter_passed(students_data)
    failed_count = count_failed(students_data)
    
    print(f"Средний балл: {average_grade:.2f}")
    print(f"Высший балл: {highest_value}")
    print(f"Низший балл: {lowest_value}")
    print(f"Медианный балл: {median_grade:.2f}")
    print(f"Размах оценок: {range_value}")
    print(f"Сдали экзамен: {', '.join(passed_students)}")
    print(f"Не сдали экзамен: {failed_count}")

if __name__ == "__main__":
    main()