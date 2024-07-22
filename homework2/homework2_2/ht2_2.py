try:
    with open('input.txt', 'r', encoding='utf-8') as f_input:
        lines = f_input.readlines()

    chars_to_remove = input("Введите символы для удаления справа (без пробелов): ")
    chars_to_remove += ';'

    modified_lines = []
    for line in lines:
        modified_line = line.rstrip(chars_to_remove)

        modified_lines.append(modified_line[::-1])

    with open('output.txt', 'w', encoding='utf-8') as f_output:
        f_output.writelines(modified_lines)

    print("Программа успешно завершила выполнение.")

except FileNotFoundError:
    print("Ошибка: файл input.txt не найден.")
except Exception as e:
    print(f"Ошибка при выполнении программы: {e}")
