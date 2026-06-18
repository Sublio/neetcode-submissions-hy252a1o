class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.anti_diag = 0

    def move(self, row: int, col: int, player: int) -> int:
        val = 1 if player == 1 else -1
        
        self.rows[row] += val
        self.cols[col] += val
        
        if row == col:
            self.diag += val
        
        if row + col == self.n - 1:
            self.anti_diag += val
        
        target = self.n if player == 1 else -self.n
        
        if (self.rows[row] == target or 
            self.cols[col] == target or 
            self.diag == target or 
            self.anti_diag == target):
            return player
        
        return 0