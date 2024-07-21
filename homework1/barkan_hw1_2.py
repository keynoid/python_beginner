def number_to_words(n):
    ones = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    teens = ["", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    tens = ["", "десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    hundreds = ["", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]

    if n == 0:
        return "ноль"

    units = n % 10
    tens_digit = (n // 10) % 10
    hundreds_digit = (n // 100) % 10

    result = ""
    if hundreds_digit != 0:
        result += hundreds[hundreds_digit] + " "
    if tens_digit == 1:
        result += teens[units] + " "
    else:
        if tens_digit != 0:
            result += tens[tens_digit] + " "
        if units != 0:
            result += ones[units] + " "

    return result.strip()

number = input("Введите число от 1 до 999: ")
if number.isdigit():
    number = int(number)
    if 1 <= number <= 999:
        words = number_to_words(number)
        print(f"Число {number} прописью: {words}")
    else:
        print("Число должно быть от 1 до 999.")
else:
    print("Ошибка: введено некорректное значение.")
