from typing import List


def shaker_sort(lst: List[int]) -> List[int]:
    """Sorts a list with int values using shaker sort algorithm.

    Args:
        lst (List[int]): list of integers

    Returns:
        List[int]: sorted (in ascending order) list of integers
    """
    lst = lst.copy()

    left_bound = 0
    right_bound = len(lst) - 1
    while left_bound < right_bound:
        # forward shaker step
        for idx in range(left_bound, right_bound):
            if lst[idx] > lst[idx+1]:
                lst[idx], lst[idx+1] = lst[idx+1], lst[idx]
        
        left_bound += 1
        # backward shaker step
        for idx in reversed(range(left_bound, right_bound)):
            if lst[idx] < lst[idx-1]:
                lst[idx], lst[idx-1] = lst[idx-1], lst[idx]
        
        right_bound -= 1
    return lst
