class Solution:
    def maxDifference(self, s: str) -> int:
        cnt = Counter(s)
    
        odd_freqs = [v for v in cnt.values() if v % 2 == 1]
        even_freqs = [v for v in cnt.values() if v % 2 == 0]
        
        if not odd_freqs or not even_freqs:
            return -1
        
        max_odd = max(odd_freqs)
        min_even = min(even_freqs)
        
        return max_odd - min_even
            