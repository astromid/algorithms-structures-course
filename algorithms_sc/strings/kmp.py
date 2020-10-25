from typing import List

from .utils import CmpCountStr


def get_pi_function(pattern: CmpCountStr) -> List[int]:
    """Calculate prefix function for pattern string.

    Args:
        pattern (CmpCountStr): pattern string

    Returns:
        List[int]: List with values of prefix function
    """
    pi_func = [0] * len(pattern)
    prefix_pos, suffix_pos = 0, 1
    while suffix_pos < len(pattern):
        if pattern[suffix_pos] == pattern[prefix_pos]:
            # if there is coincidence we increase len by 1 and shift position indexes
            pi_func[suffix_pos] = prefix_pos + 1
            suffix_pos += 1
            prefix_pos += 1
        elif prefix_pos == 0:
            # pi remains zero
            suffix_pos += 1
        else:
            # if we already check prefix/suffix with length > 1 then we need to decrease length
            # we can check just previous success length
            prefix_pos = pi_func[prefix_pos - 1]
    return pi_func


def kmp(needle: CmpCountStr, haystack: CmpCountStr) -> List[int]:
    """Performs search of string in text with Knuth-Morris-Pratt algorithm.

    Args:
        needle (CmpCountStr): substring to search
        haystack (CmpCountStr): string (text) to search in

    Returns:
        List[int]: positions of entries of substring in string (empty if there's no substring in string)
    """
    # 1 шаг - prefix function calculation
    pi_func = get_pi_function(needle)
    # 2 шаг - substring search
    positions = []
    # we use 2 position indexes
    needle_pos, haystack_pos = 0, 0
    while haystack_pos < len(haystack):
        if needle[needle_pos] == haystack[haystack_pos]:
            # if we have a coincidence and needle_pos + 1 = len(needle), we have our substring
            if needle_pos + 1 == len(needle):
                positions.append(haystack_pos - len(needle) + 1)
                needle_pos = 0
                continue
            # otherwise, continue to compare chars
            needle_pos += 1
            haystack_pos += 1
        # if needle postion is already zero we need just to shift pattern forward
        elif needle_pos == 0:
            haystack_pos += 1
        # otherwise, we use position for previous success char in prefix function table
        else:
            needle_pos = pi_func[needle_pos - 1]
    return positions
