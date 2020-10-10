from numpy.random import default_rng

ALPHABET = ('G', 'A', 'V', 'I', 'L', 'P', 'S', 'T', 'C', 'M', 'D', 'N', 'E', 'Q', 'K', 'R', 'H', 'F', 'Y', 'W')


class CmpCountStr(str):
    '''String wrapper class with comparsion counter.'''

    cmp_counter = 0

    def __init__(self, string: str) -> None:
        super().__init__()
        self.string = string
    
    def __eq__(self, other: object) -> bool:
        CmpCountStr.cmp_counter += 1
        return self.string.__eq__(other)
    
    def __ne__(self, other: object) -> bool:
        CmpCountStr.cmp_counter += 1
        return self.string.__ne__(other)
    
    def __getitem__(self, sl: slice):
        return CmpCountStr(self.string[sl])
    
    def __iter__(self):
        return iter(self.string)
    
    def __hash__(self) -> int:
        return hash(self.string)


def generate_protein_text(length: int) -> CmpCountStr:
    rng = default_rng()
    chars = rng.choice(ALPHABET, size=length)
    return CmpCountStr(''.join(chars))
