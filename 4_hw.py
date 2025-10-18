#задача 1
class Rectangle:
    """Класс, описывающий прямоугольник."""

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        """Вычисляет площадь прямоугольника."""
        return self.width * self.height

    def perimeter(self) -> float:
        """Вычисляет периметр прямоугольника."""
        return 2 * (self.width + self.height)

rect1 = Rectangle(5, 10)
rect2 = Rectangle(3.5, 7.2)
rect3 = Rectangle(9, 4)

for i, rect in enumerate([rect1, rect2, rect3], start=1):
    print(f"Прямоугольник {i}:")
    print(f"  Площадь = {rect.area()}")
    print(f"  Периметр = {rect.perimeter()}\n")

#задача 2
class Math:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def addition(self) -> None:
        print(f"Сложение: {self.a} + {self.b} = {self.a + self.b}")

    def subtraction(self) -> None:
        print(f"Вычитание: {self.a} - {self.b} = {self.a - self.b}")

    def multiplication(self) -> None:
        print(f"Умножение: {self.a} * {self.b} = {self.a * self.b}")

    def division(self) -> None:
        if self.b != 0:
            print(f"Деление: {self.a} / {self.b} = {self.a / self.b}")
        else:
            print("Ошибка: деление на ноль!")

#задача 3
class SidebarButton:
    def __init__(self, text: str, button_type: str = "Кнопка", locator: str = ""):
        self.text = text
        self.button_type = button_type
        self.locator = locator

    def click(self) -> str:
        """Метод, имитирующий клик по кнопке."""
        return f"Клик по кнопке '{self.text}'"


#Объекты для каждой кнопочкииии
buttons = [
    SidebarButton("Text Box"),
    SidebarButton("Check Box"),
    SidebarButton("Radio Button"),
    SidebarButton("Web Tables"),
    SidebarButton("Buttons"),
    SidebarButton("Links"),
    SidebarButton("Broken Links - Images"),
    SidebarButton("Upload and Download"),
    SidebarButton("Dynamic Properties")
]
for btn in buttons:
    print(f"Название: {btn.text}, Тип: {btn.button_type}")
    print(btn.click())
    print()

#задача 4 не понял для чего создавать новый файл и как потом его скинуть если что, поэтому пусть будет тут тоже(
class Car:
    def __init__(self, color: str = "", car_type: str = "", year: int = 0):
        self.color = color
        self.type = car_type
        self.year = year

    def start(self) -> None:
        print("Автомобиль заведен")

    def stop(self) -> None:
        print("Автомобиль заглушен")

    def set_year(self, year: int) -> None:
        self.year = year
        print(f"Год выпуска установлен: {self.year}")

    def set_type(self, car_type: str) -> None:
        self.type = car_type
        print(f"Тип автомобиля установлен: {self.type}")

    def set_color(self, color: str) -> None:
        self.color = color
        print(f"Цвет автомобиля установлен: {self.color}")
