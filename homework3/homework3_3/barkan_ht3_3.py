import json

try:
    with open('input.txt', 'r', encoding='utf-8') as file:
        data = json.load(file)

    course_name = input("Введите название курса: ").strip()
    students_on_course = []

    for student, courses in data.items():
        if course_name in courses:
            students_on_course.append(student)

    if students_on_course:
        print(f"Студенты на курсе '{course_name}':")
        for student in students_on_course:
            print(student)
    else:
        print(f"На курс '{course_name}' не записан ни один студент.")

except FileNotFoundError:
    print("Ошибка: файл input.txt не найден.")
except Exception as e:
    print(f"Ошибка при выполнении программы: {e}")

