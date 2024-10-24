# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`)
# и методы (`make_sound()`, `eat()`) для всех животных.
#
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса
# `Animal`. Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный
# звук для `make_sound()`).
#
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список
# животных и вызывает метод `make_sound()` для каждого животного.


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} издаёт звук")

    def eat(self):
        print(f"{self.name} ест")

class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        print(f"{self.name} чирикает")

    def fly(self):
        print(f"{self.name} летит с размахом крыльев {self.wind_span} м")

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} рычит")

    def run(self):
        print(f"{self.name} бежит")

class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        print(f"{self.name} шипит")

    def crawl(self):
        print(f"{self.name} ползет")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

parrot = Bird(name="Попугай", age=3, wing_span=0.5)
tiger = Mammal(name="Тигр", age=5, fur_color="Оранжевый")
snake = Reptile(name="Змея", age=2, scale_type="Гладкая")

animals = [parrot, tiger, snake]

animal_sound(animals)
