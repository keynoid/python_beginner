try:
    n = int(input('Input number of rows. '))
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))
except Exception:
    print("Incorrect input. Please try again.")