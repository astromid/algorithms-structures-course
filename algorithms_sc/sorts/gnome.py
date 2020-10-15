from typing import List


def gnome_sort(lst: List[int]) -> List[int]:
    '''Sorts a list with int values using Gnome sort algorithm.

    Args:
        lst (List[int]): list of integers

    Returns:
        List[int]: sorted (in ascending order) list of integers
    '''
    lst = lst.copy()

    idx = 1
    reversal_index = 2
    while idx < len(lst):
        # normal situation, just shift indexes
        if lst[idx-1] < lst[idx]:
            idx = reversal_index
            reversal_index += 1
        # swap elements and go one position behind
        else:
            lst[idx-1], lst[idx] = lst[idx], lst[idx-1]
            idx -= 1
            # if idx = 0 we can jump to previous position where we turned around
            if idx == 0:
                idx = reversal_index
                reversal_index += 1
    return lst
