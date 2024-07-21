students = {}

with open('input.txt', 'r') as text_file:
    for line in text_file:
        try:
            name, mark = line.split(',')
            students[name] = mark.strip()
        except Exception:
            print(f'Invalid input - {line}')


average = sum([int(mark) for mark in students.values()]) / len(students)

with open('output.txt', 'w') as text_file:
    text_file.write(f'Average mark - {average}\n')
    for name, mark in students.items():
        if int(mark) > average:
            text_file.write(f'{name} - {mark}\n')