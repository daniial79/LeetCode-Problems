def is_valid_sudoku(self, board: list[list[str]]) -> bool:
    for i in range(len(board)):
        if not is_valid(board[i]):
            return False
        
    for i in range(len(board)):
        container = []
        for j in range(len(board)):
            container.append(board[j][i])
        if not is_valid(container):
            return False
        
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            if not is_valid(grid_to_list(board, i, j)):
                return False
    
    return True


def is_valid(arr: list[str]) -> bool:
    existence_check = {}
    for char in arr:
        if char == ".":
            continue
        
        if existence_check.get(char):
            return False
        else:
            existence_check.setdefault(char, True)
    return True


def grid_to_list(board: list[list[str]], x: int, y: int) -> bool:
    listed_grid = []
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            listed_grid.append(board[j][i])
    return listed_grid