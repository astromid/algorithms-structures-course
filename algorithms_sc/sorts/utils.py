import random
from typing import List


def one_bubble_step(lst: List[int], ascending=True) -> List[int]:
    lst = lst.copy()
    for idx in range(len(lst)-1):
        if (ascending and lst[idx] > lst[idx+1]) or (not ascending and lst[idx] < lst[idx+1]):
            lst[idx], lst[idx+1] = lst[idx+1], lst[idx]
    return lst


def generate_stand(length: int) -> List[List[int]]:
    stand: List[List[int]] = []
    random_list = random.sample(range(length ** 2), length)
    sorted_list = sorted(random_list)
    reversed_sorted_list = list(reversed(sorted_list))
    
    partially_sorted_list = random_list.copy()
    for _ in range(length):
        partially_sorted_list = one_bubble_step(partially_sorted_list, ascending=False)
        stand.append(partially_sorted_list)
    
    stand = list(reversed(stand))
    # central element of the stand
    stand.append(random_list)

    partially_sorted_list = random_list.copy()
    for _ in range(length):
        partially_sorted_list = one_bubble_step(partially_sorted_list)
        stand.append(partially_sorted_list)
    return stand
