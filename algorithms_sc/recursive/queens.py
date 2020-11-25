from typing import List, Tuple


class ChessDesk:

    def __init__(self, desk_size: int) -> None:
        self.desk_size = desk_size
        self.desk = [-1] * desk_size
        self.horizontals = [True] * desk_size
        self.increasing_diags = {diag_const: True for diag_const in range(0, 2 * desk_size - 1)}
        self.decreasing_diags = {diag_const: True for diag_const in range(1 - desk_size, desk_size)}
        self.try_count = 0
        self.is_solved = False

    def is_position_safe(self, h_idx: int, v_idx: int) -> bool:
        return self.horizontals[h_idx] and self.increasing_diags[v_idx + h_idx] and self.decreasing_diags[v_idx - h_idx]
    
    def set_queen(self, h_idx: int, v_idx: int) -> None:
        self.desk[v_idx] = h_idx
        self.horizontals[h_idx] = False
        self.increasing_diags[v_idx + h_idx] = False
        self.decreasing_diags[v_idx - h_idx] = False
    
    def remove_queen(self, h_idx: int, v_idx: int) -> None:
        self.desk[v_idx] = -1
        self.horizontals[h_idx] = True
        self.increasing_diags[v_idx + h_idx] = True
        self.decreasing_diags[v_idx - h_idx] = True



def solve_queens(desk_size: int) -> Tuple[int, List[int]]:
    desk = ChessDesk(desk_size)
    try_position(0, desk)
    if desk.is_solved:
        return desk
    else:
        return -1


def try_position(v_idx: int, desk: ChessDesk) -> None:
    h_idx = -1
    desk.try_count += 1
    while not desk.is_solved and h_idx < desk.desk_size - 1:
        h_idx += 1
        if desk.is_position_safe(h_idx, v_idx):
            desk.set_queen(h_idx, v_idx)
            if v_idx < desk.desk_size - 1:
                try_position(v_idx + 1, desk)
                # backtracking - remove last queen
                if not desk.is_solved:
                    desk.remove_queen(h_idx, v_idx)
            else:
                desk.is_solved = True
