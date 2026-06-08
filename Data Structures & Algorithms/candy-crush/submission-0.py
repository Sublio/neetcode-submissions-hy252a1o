class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m, n = len(board), len(board[0])
        
        while True:
            to_crush = [[False] * n for _ in range(m)]
            crushed = False
            
            for r in range(m):
                for c in range(n - 2):
                    val = board[r][c]
                    if val != 0 and board[r][c+1] == val and board[r][c+2] == val:
                        to_crush[r][c] = to_crush[r][c+1] = to_crush[r][c+2] = True
                        crushed = True
            
            for c in range(n):
                for r in range(m - 2):
                    val = board[r][c]
                    if val != 0 and board[r+1][c] == val and board[r+2][c] == val:
                        to_crush[r][c] = to_crush[r+1][c] = to_crush[r+2][c] = True
                        crushed = True
            
            for r in range(m):
                for c in range(n):
                    if to_crush[r][c]:
                        board[r][c] = 0
            
            if not crushed:
                break
            
            for c in range(n):
                values = []
                for r in range(m-1, -1, -1):
                    if board[r][c] != 0:
                        values.append(board[r][c])
                
                for r in range(m-1, -1, -1):
                    if values:
                        board[r][c] = values.pop(0)
                    else:
                        board[r][c] = 0
        
        return board