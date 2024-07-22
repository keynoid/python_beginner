def count_ways(n):
    if n == 0 or n == 1:
        return 1

    ways = [0] * (n + 1)
    ways[0] = 1
    ways[1] = 1

    for i in range(2, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]

    return ways[n]

try:
    n = int(input("Введите количество ступенек (n): "))
    if n < 0:
        print("Число ступенек должно быть неотрицательным.")
    else:
        ways = count_ways(n)
        print(f"Количество способов подняться на {n} ступенек равняется: {ways}")

except ValueError:
    print("Ошибка: введите натуральое число.")
