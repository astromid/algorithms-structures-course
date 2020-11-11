from typing import List


def make_heap(lst: List[int], size: int, idx: int) -> List[int]:
    """Create max-heap at index idx

    Args:
        lst (List[int]): array with integers
        size (int): size of the heap
        idx (int): current node index

    Returns:
        List[int]: max-heap list
    """
    # init root (largest element)
    root_idx = idx
    # calculate indexes of left and right leafs
    left_node_idx = 2 * idx + 1
    right_node_idx = 2 * idx + 2
    # check left leaf for new root
    if left_node_idx < size and lst[root_idx] < lst[left_node_idx]:
        root_idx = left_node_idx
    # check right leaf for new root
    if right_node_idx < size and lst[root_idx] < lst[right_node_idx]:
        root_idx = right_node_idx
    # if need, swap root and make recursive call
    if root_idx != idx:
        lst[idx], lst[root_idx] = lst[root_idx], lst[idx]
        # make heap at new root index
        make_heap(lst, size, root_idx)
    return lst


def heap_sort(lst: List[int]) -> List[int]:
    """Sort array with heap sort algorithm.

    Args:
        lst (List[int]): list of integers

    Returns:
        List[int]: sorted list
    """
    size = len(lst)
    # create max-heap in bottom-top way
    for idx in range(size // 2 - 1, -1, -1):
        make_heap(lst, size, idx)
    # swap max elements one-by-one and support max-heap at index 0
    for idx in range(size - 1, 0, -1):
        lst[idx], lst[0] = lst[0], lst[idx]
        make_heap(lst, idx, 0)
    return lst