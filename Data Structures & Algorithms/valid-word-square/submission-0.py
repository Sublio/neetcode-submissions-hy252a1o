class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        if not words:
            return True
        
        numRows = len(words)
        
        for i in range(numRows):
            for j in range(len(words[i])):
                if j >= numRows or i >= len(words[j]):
                    return False
                if words[i][j] != words[j][i]:
                    return False
        
        return True

        
        