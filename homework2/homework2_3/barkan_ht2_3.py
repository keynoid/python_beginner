try:
    with open('input1.txt', 'r', encoding='utf-8') as f1, open('input2.txt', 'r', encoding='utf-8') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    combined_lines = sorted(lines1 + lines2)

    with open('output.txt', 'w', encoding='utf-8') as f_output:
        f_output.writelines(combined_lines)

    print("Программа успешно завершила выполнение.")

except FileNotFoundError:
    print("Ошибка: один из файлов (input1.txt или input2.txt) не найден.")
except Exception as e:
    print(f"Ошибка при выполнении программы: {e}")

