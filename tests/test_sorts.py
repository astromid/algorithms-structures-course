import random
from typing import List

import pytest
from algorithms_sc.sorts import gnome_sort, heap_sort, shaker_sort, bitonic_sort

TEST_LEN = 300
TEST_NUM = 200

TEST_ARRAYS = [random.sample(range(TEST_LEN ** 2), TEST_LEN) for _ in range(TEST_NUM)]
EXPECTED = [sorted(array) for array in TEST_ARRAYS]


@pytest.mark.parametrize('array, expected', zip(TEST_ARRAYS, EXPECTED))
def test_shaker_sort(array: List[int], expected: List[int]) -> None:
    sorted_array = shaker_sort(array)
    assert sorted_array == expected


@pytest.mark.parametrize('array, expected', zip(TEST_ARRAYS, EXPECTED))
def test_gnome_sort(array: List[int], expected: List[int]) -> None:
    sorted_array = gnome_sort(array)
    assert sorted_array == expected


@pytest.mark.parametrize('array, expected', zip(TEST_ARRAYS, EXPECTED))
def test_heap_sort(array: List[int], expected: List[int]) -> None:
    sorted_array = heap_sort(array)
    assert sorted_array == expected


@pytest.mark.parametrize('array, expected', zip(TEST_ARRAYS, EXPECTED))
def test_bitonic_sort(array: List[int], expected: List[int]) -> None:
    sorted_array = bitonic_sort(array)
    assert sorted_array == expected
