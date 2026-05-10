class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        needed = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
        
        result = float('inf')
        for ch, need in needed.items():
            if count[ch] < need:
                return 0
            result = min(result, count[ch] // need)
        
        return result
        