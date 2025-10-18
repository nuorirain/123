# Задача 1
def task_1() -> None:
  
    num_int: int = 10
    num_float: float = 3.14
    text_str: str = "Автоматизация тестирования"
    list_values: list = [1, 2, 3, 4, 5]
    is_active: bool = True

    print(type(num_int))
    print(type(num_float))
    print(type(text_str))
    print(type(list_values))
    print(type(is_active))



task_1()


# Задача 2
def task_2() -> None:
    a = [1, 2, 3, 5, 8, 13, 21]
    # Вывод первых трёх элементов списка
    print(a[:3])
    # Примечание: это последовательность Фибоначчи



task_2()


# Задача 3
def task_3(number: int) -> int:
    """Функция возвращает квадрат переданного числа"""
    return number ** 2



print(task_3(5))
