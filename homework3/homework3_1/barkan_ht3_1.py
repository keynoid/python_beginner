try:
    with open('cities.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    min_population = int(input("Введите минимальное значение населения: "))

    filtered_cities = []
    for line in lines:
        city_population = line.strip().split(':')
        city = city_population[0]
        population = int(city_population[1])
        if population > min_population:
            filtered_cities.append(city)

    filtered_cities.sort()

    with open('filtered_cities.txt', 'w', encoding='utf-8') as file:
        for city in filtered_cities:
            file.write(city + '\n')

    print("Программа успешно завершила выполнение.")

except FileNotFoundError:
    print("Ошибка: файл cities.txt не найден.")
except ValueError:
    print("Ошибка: введено некорректное значение для населения.")
except Exception as e:
    print(f"Ошибка при выполнении программы: {e}")

