class Pet:
    def __init__(self, name: str, type: str, age: int, sex: str):
        self._name = name
        self._type = type
        self._age = age
        self._sex = sex

    def get_info(self):
        print(f" Имя: {self._name}\n Вид: {self._type}\n Возраст: {self._age}\n Пол: {self._sex}")

class Dog(Pet):
    def __init__(self, name: str, type: str, age: int, sex: str, race: str):
        super().__init__(name, type, age, sex)
        self._race = race

    def get_info(self):
        super().get_info()
        print(f" Порода: {self._race}")

    def bark(self):
        print(f" {self._name} говорит: Гав!\n")    

class Cat(Pet):
    def __init__(self, name: str, type: str, age: int, sex: str, color: str):
        super().__init__(name, type, age, sex)
        self._color = color

    def get_info(self):
        super().get_info()
        print(f" Цвет: {self._color}")

    def meow(self):
        print(f" {self._name} говорит: Мяу!\n")

muhtar = Dog("Muhtar", "dog", 10, "male", "shepherd")
muhtar.get_info()
muhtar.bark()
murka = Cat("Murka", "Cat", 5, "female", "black")
murka.get_info()
murka.meow()