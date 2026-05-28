class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        diff1 = 0 
        diff2 = 0 
        
        for i in range(n):
            expected1 = '0' if i % 2 == 0 else '1'
            if s[i] != expected1:
                diff1 += 1
            
            expected2 = '1' if i % 2 == 0 else '0'
            if s[i] != expected2:
                diff2 += 1
        
        return min(diff1, diff2)
        