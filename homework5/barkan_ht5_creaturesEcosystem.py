import random

class Species:
    def __init__(self, name, size, food_type, habitat, lifespan):
        self.name = name
        self.size = size
        self.food_type = food_type
        self.habitat = habitat
        self.lifespan = lifespan

    def __str__(self):
        return (f"Вид: {self.name}, Размер: {self.size}, Тип пищи: {self.food_type}, "
                f"Среда обитания: {self.habitat}, Продолжительность жизни: {self.lifespan}")

class Animal:
    def __init__(self, species, age=0, hunger=50, gender=None):
        self.species = species
        self.age = age
        self.hunger = hunger
        self.gender = gender if gender else random.choice(['Самец', 'Самка'])

    def age_one_year(self):
        self.age += 1

    def __str__(self):
        return (f"Животное вида: {self.species.name}, Возраст: {self.age}, Сытость: {self.hunger}, Пол: {self.gender}")

class Ecosystem:
    def __init__(self):
        self.species_list = [
            Species("Креветка", size=1, food_type="растительная", habitat="вода", lifespan=2),
            Species("Орел", size=10, food_type="животная", habitat="воздух", lifespan=35),
            Species("Тигр", size=40, food_type="животная", habitat="земля", lifespan=25),
            Species("Лошадь", size=60, food_type="растительная", habitat="земля", lifespan=27)
        ]
        self.animals = []
        self.plant_food = 1395

    def add_animal(self, species_name, age=0, hunger=50, gender=None):
        species = next((s for s in self.species_list if s.name == species_name), None)
        if species:
            new_animal = Animal(species, age, hunger, gender)
            self.animals.append(new_animal)
            print(f"Добавлено новое животное: {new_animal}")
        else:
            print(f"Вид {species_name} не найден.")

    def increase_plant_food(self, amount):
        self.plant_food += amount
        print(f"Запас растительной пищи увеличен на {amount}. Запасов всего: {self.plant_food}")

    def view_animals(self):
        if self.animals:
            print("Текущие животные:")
            for animal in self.animals:
                print(animal)
        else:
            print("Животные отсутствуют.")

    def view_species(self):
        for species in self.species_list:
            print(species)

    def view_animal_info(self, animal_id):
        animal = next((a for a in self.animals if id(a) == animal_id), None)
        if animal:
            print(animal)
        else:
            print("Животное не найдено.")

    def attempt_reproduction(self, animal_id1, animal_id2):
        animal1 = next((a for a in self.animals if id(a) == animal_id1), None)
        animal2 = next((a for a in self.animals if id(a) == animal_id2), None)

        if animal1 and animal2 and animal1.species == animal2.species and animal1.gender != animal2.gender:
            if animal1.species.habitat == 'вода' and animal1.hunger > 50 and animal2.hunger > 50:
                self.animals.extend([Animal(animal1.species, hunger=23) for _ in range(10)])
                print("Создано 10 новых водных животных.")
            elif animal1.species.habitat == 'воздух' and animal1.hunger > 42 and animal1.age > 3 and animal2.hunger > 42 and animal2.age > 3:
                self.animals.extend([Animal(animal1.species, hunger=64) for _ in range(4)])
                print("Создано 4 новых воздушных животных.")
            elif animal1.species.habitat == 'земля' and animal1.hunger > 20 and animal1.age > 5 and animal2.hunger > 20 and animal2.age > 5:
                self.animals.extend([Animal(animal1.species, hunger=73) for _ in range(2)])
                print("Создано 2 новых земных животных.")
            else:
                print("Условия для размножения не выполнены.")
        else:
            print("Животные не одного вида или имеют одинаковый пол.")

    def time_step(self):
        for animal in self.animals[:]:
            animal.age_one_year()
            if animal.age > animal.species.lifespan:
                self.animals.remove(animal)
                self.plant_food += animal.species.size
                print(f"Животное {animal} превратилось в растительную пищу.")
            elif animal.species.food_type == "растительная":
                if self.plant_food > 0:
                    animal.hunger = min(100, animal.hunger + 26)
                    self.plant_food -= 1
            else:
                if random.random() < 0.5:
                    animal.hunger = min(100, animal.hunger + 53)
                else:
                    animal.hunger = max(0, animal.hunger - 16)
            if animal.hunger < 10:
                self.animals.remove(animal)
                self.plant_food += animal.species.size
                print(f"Животное {animal} превратилось в растительную пищу из-за голода.")

    def help(self):
        print("""
Команды:
add_animal <вид> [возраст] [сытость] [пол] - Добавить новое животное
increase_plant_food <количество> - Увеличить запас растительной пищи
view_animals - Посмотреть всех животных
view_species - Посмотреть все виды животных
view_animal_info <animal_id> - Посмотреть информацию о конкретном животном
attempt_reproduction <animal_id1> <animal_id2> - Попробовать размножить двух животных одного вида
time_step - Пройти шаг времени
exit - Выйти
""")

def main():
    ecosystem = Ecosystem()

    print("Добро пожаловать в симуляцию экосистемы!")
    print("Вот виды животных на планете:")
    ecosystem.view_species()

    while True:
        command = input("Введите команду (наберите 'help' для списка команд): ").strip()

        if command.startswith('add_animal'):
            _, species_name, *args = command.split()
            age = int(args[0]) if len(args) > 0 else 0
            hunger = int(args[1]) if len(args) > 1 else 50
            gender = args[2] if len(args) > 2 else None
            ecosystem.add_animal(species_name, age, hunger, gender)
        elif command.startswith('increase_plant_food'):
            _, amount = command.split()
            ecosystem.increase_plant_food(int(amount))
        elif command == 'view_animals':
            ecosystem.view_animals()
        elif command == 'view_species':
            ecosystem.view_species()
        elif command.startswith('view_animal_info'):
            _, animal_id = command.split()
            ecosystem.view_animal_info(int(animal_id))
        elif command.startswith('attempt_reproduction'):
            _, animal_id1, animal_id2 = command.split()
            ecosystem.attempt_reproduction(int(animal_id1), int(animal_id2))
        elif command == 'time_step':
            ecosystem.time_step()
        elif command == 'help':
            ecosystem.help()
        elif command == 'exit':
            print("Выход из игры.")
            break
        else:
            print("Неизвестная команда. Введите 'help' для списка команд.")

if __name__ == "__main__":
    main()
#
# add_animal Лошадь 2 50 Самка
# add_animal Лошадь 2 50 Самец
# add_animal Тигр 10 100 Самка
# add_animal Тигр 2 70 Самец