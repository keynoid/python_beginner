import json

try:
    with open('input.txt', 'r', encoding='utf-8') as file:
        sales_data = json.load(file)

    total_sales = {}

    for store_data in sales_data.values():
        for product, amount in store_data.items():
            if product in total_sales:
                total_sales[product] += amount
            else:
                total_sales[product] = amount

    with open('output.txt', 'w', encoding='utf-8') as file:
        for product, total_amount in total_sales.items():
            file.write(f"{product}: {total_amount}\n")

    print("Результаты успешно записаны в файл output.txt.")

except FileNotFoundError:
    print("Ошибка: файл input.txt не найден.")
except Exception as e:
    print(f"Ошибка при выполнении программы: {e}")
