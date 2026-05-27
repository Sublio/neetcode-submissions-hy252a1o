class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        total_ones = s.count('1')
        zeros_left = 0
        ones_in_left = 0
        max_score = 0
        
        for i in range(n - 1):
            if s[i] == '0':
                zeros_left += 1
            else:
                ones_in_left += 1
            ones_right = total_ones - ones_in_left
            score = zeros_left + ones_right
            max_score = max(max_score, score)
        
        return max_score
            