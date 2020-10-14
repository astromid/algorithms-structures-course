from collections import defaultdict
from typing import Dict

from .utils import CmpCountStr


def get_offset_table(pattern: CmpCountStr) -> Dict[str, int]:
    '''Calculate offset table for the pattern.'''
    # default value for other chars - lenght of needle string
    offset_table = defaultdict(lambda: len(pattern))
    # don't count last char
    for idx, char in enumerate(pattern[:-1]):
        offset_table[char] = len(pattern) - idx - 1
    return offset_table


def boyer_moore(needle: CmpCountStr, haystack: CmpCountStr) -> int:
    '''Return first position of needle in haystack (or -1 if there isn't needle in haystack).'''

    offset_table = get_offset_table(needle)
    
    position = -1
    current_pos = 0
    while current_pos < len(haystack) - len(needle) + 1:
        # successful comparsion flag
        was_coincidence = False
        # compare in reverse order
        for idx in reversed(range(len(needle))):
            if needle[idx] == haystack[current_pos + idx]:
                was_coincidence = True
            else:
                # we need to shift our position in haystack and break inner cycle
                # if there was as coincidence before, we use an offset for last needle char
                if was_coincidence:
                    current_offset = offset_table[needle[-1]]
                # if not, we use an offset for char from haystack
                else:
                    current_offset = offset_table[haystack[current_pos + idx]]
                current_pos += current_offset
                break
        # if there wasn't break - we find needle in current position
        else:
            position = current_pos
            break
    return position
