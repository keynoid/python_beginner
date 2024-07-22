def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))

    result = gcd(a, b)

    print(f"НОД чисел {a} и {b} равен {result}.")

except ValueError:
    print("Ошибка: введите целые числа заново.")
except Exception as e:
    print(f"Ошибка: {e}")

