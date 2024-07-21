def sum_of_digits(n):
    sum_digits = 0
    while n > 0:
        sum_digits += n % 10
        n //= 10
    return sum_digits

try:
    number = int(input("Введите число: "))
    while number > 9:
        number = sum_of_digits(number)
    print(f"Однозначная сумма цифр: {number}")
except ValueError:
    print("Ошибка: введено некорректное значение.")
