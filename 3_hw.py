#задача 1
def task_2_1(a: float, b: float) -> None:
    if a > b:
        print(f"Наибольшее число: {a}")
    elif b > a:
        print(f"Наибольшее число: {b}")
    else:
        print("Числа равны")

#задача 2
def task_3_1(a: int, b: int) -> None:
    if abs(a - b) == 135:
        print("yes")
    else:
        print("no")
#задача 3
def task_4_1(month: int) -> None:
    if month in (12, 1, 2):
        print("зима")
    elif month in (3, 4, 5):
        print("весна")
    elif month in (6, 7, 8):
        print("лето")
    elif month in (9, 10, 11):
        print("осень")
    else:
        print("Ошибка: введите число от 1 до 12")

#задача 4
def task_5_1(a: int, b: int, c: int) -> None:
    """Проверяет, больше ли все три числа 10."""
    if a > 10 and b > 10 and c > 10:
        print("yes")
    else:
        print("no")

#задача 5 дополнительное *
def task_6(numbers: list[int]) -> None:
    if len(numbers) != 5:
        print("Ошибка: список должен содержать 5 чисел")
        return

    positive_count = sum(1 for n in numbers if n > 0)
    print(f"Количество положительных чисел: {positive_count}")
