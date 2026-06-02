class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
    
        for i in range(rowIndex):
            next_row = [1]
            for j in range(len(row) - 1):
                next_row.append(row[j] + row[j + 1])
            next_row.append(1)
            row = next_row
        
        return row
        