class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        if not picture or not picture[0]:
            return 0
        
        m, n = len(picture), len(picture[0])
        
        row_count = [0] * m
        col_count = [0] * n
        
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    row_count[i] += 1
                    col_count[j] += 1
        
        lonely_pixels = 0
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B' and row_count[i] == 1 and col_count[j] == 1:
                    lonely_pixels += 1
        
        return lonely_pixels
        