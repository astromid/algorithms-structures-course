from algorithms_sc.strings.boyer_moore import get_offset_table, boyer_moore
from algorithms_sc.strings.kmp import get_pi_function, kmp
from algorithms_sc.strings.utils import CmpCountStr
import pytest

NEEDLES = (
    CmpCountStr('success'),
    CmpCountStr('data'),
    CmpCountStr('GAGA'),
    CmpCountStr(' now')
)

HAYSTACKS = (
    CmpCountStr('It was very successful!'),
    CmpCountStr('Your personal data have been removed.'),
    CmpCountStr('GGGAAGQRKTGGGKRDNVALASFRLLAFSASKASFGVASGAALG'),
    CmpCountStr('Something strange is going on now'),
)

OFFSET_TABLES = (
    {'s': 1, 'e': 2, 'c': 3, 'u': 5},
    {'t': 1, 'a': 2, 'd': 3},
    {'G': 1, 'A': 2},
    {'w': 4, 'o': 1, 'n': 2, ' ': 3},
)

POSITIONS = (12, 14, -1, 29)


@pytest.mark.parametrize('needle, expected_table', zip(NEEDLES, OFFSET_TABLES))
def test_offset_table(needle, expected_table):
    offset_table = get_offset_table(needle)
    for key in offset_table.keys():
        assert offset_table[key] == expected_table[key]


@pytest.mark.parametrize('needle, haystack, expected_position', zip(NEEDLES, HAYSTACKS, POSITIONS))
def test_boyer_moore(needle, haystack, expected_position):
    position = boyer_moore(needle, haystack)
    assert position == expected_position
