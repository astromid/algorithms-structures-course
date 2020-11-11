from typing import List, Optional


def bitonic_merge(lst: List[int], left_idx: int, size: int, ascending: bool = True) -> List[int]:
    if size > 1:
        half_size = size // 2
        for i in range(left_idx, left_idx + half_size):
            if (ascending and lst[i] > lst[i + half_size]) or (not ascending and lst[i] < lst[i + half_size]):
                lst[i], lst[i + half_size] = lst[i + half_size], lst[i]
        lst = bitonic_merge(lst, left_idx, half_size, ascending)
        lst = bitonic_merge(lst, left_idx + half_size, half_size, ascending)
    return lst


def bitonic_sort(
    lst: List[int],
    left_idx: Optional[int] = None,
    size: Optional[int] = None,
    ascending: bool = True,
) -> List[int]:
    if size is None:
        size = len(lst)
    
    if left_idx is None:
        left_idx = 0
    
    if size > 1:
        half_size = size // 2
        lst = bitonic_sort(lst, left_idx, half_size, ascending=True)
        lst = bitonic_sort(lst, left_idx + half_size, half_size, ascending=False)
        lst = bitonic_merge(lst, left_idx, size, ascending)
    return lst
