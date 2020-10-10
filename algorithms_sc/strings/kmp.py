from typing import List

from .utils import CmpCountStr


def get_pi_function(pattern: CmpCountStr) -> List[int]:
    # Расчет префикс-функции для строки
    pi_func = [0] * len(pattern)
    for idx in range(1, len(pattern)):
        # зная i-1 значение, рассчитваем i-тое значение
        k = pi_func[idx - 1]
        while pattern[idx] != pattern[k]:
            if k == 0:
                break
            k = pi_func[k - 1]
        # если не было выхода по break - значит, был выход по равенству
        else:
            k += 1
        pi_func[idx] = k
    return pi_func


def kmp(needle: CmpCountStr, haystack: CmpCountStr) -> int:
    # 1 шаг - вычисление префикс-функции
    pi_func = get_pi_function(needle)
    # 2 шаг - поиск подстроки
    position = -1
    k = 0
    for idx in range(len(haystack)):
        while needle[k] != haystack[idx]:
            if k == 0:
                break
            # если символ из строки не совпадает с символом из текста, то сдвигаемся на максимальную длину префикса
            k = pi_func[k - 1]
        # при выходе по достижении равенства
        else:
            k += 1
        if k == len(needle):
            position = idx - len(needle) + 1
            break
    return position
