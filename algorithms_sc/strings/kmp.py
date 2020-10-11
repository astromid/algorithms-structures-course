from typing import List

from .utils import CmpCountStr


def get_pi_function(pattern: CmpCountStr) -> List[int]:
    '''Calculate prefix function for pattern string.'''
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


def kmp(needle: CmpCountStr, haystack: CmpCountStr) -> int:
    # 1 шаг - prefix function calculation
    pi_func = get_pi_function(needle)
    # 2 шаг - substring search
    position = -1
    # we use 2 position indexes
    current_needle_pos, current_haystack_pos = 0, 0
    while current_haystack_pos < len(haystack):
        if needle[current_needle_pos] == haystack[current_haystack_pos]:
            # if we have a coincidence and needle_pos + 1 = len(needle), we have our substring
            if current_needle_pos == len(needle) - 1:
                position = current_haystack_pos - len(needle) + 1
                break
            # otherwise, continue to compare chars
            current_needle_pos += 1
            current_haystack_pos += 1
        # if needle postion is already zero we need just to shift pattern forward
        elif current_needle_pos == 0:
            current_haystack_pos += 1
        # otherwise, we use position for previous success char in prefix function table
        else:
            current_needle_pos = pi_func[current_needle_pos - 1]
    return position
