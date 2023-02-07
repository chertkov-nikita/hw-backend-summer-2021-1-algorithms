__all__ = (
    'is_prime',
)


def is_prime(number: int) -> bool:
    """
    Функция должна вернуть True если число является простым, иначе - False
    """
    number = abs(number)
    if number == 1 or number == 0:
        return False
    k = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            k += 1
    return k <= 0
