__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    """
    Функция возвращает отношение суммы четных элементов массив к сумме нечетных
    Пример:
    even_odd([1, 2, 3, 4, 5]) == 0.8889
    """
    try:
        result = sum(x for x in arr if x % 2 == 0) / sum(x for x in arr if x % 2 != 0)
    except ZeroDivisionError:
        result = 0
    return result
