class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        all_counts = 0
        odd_seen = False
        for k,v in cnt.items():
            all_counts += (v//2) *2
            if v %2==1:
                odd_seen = True
        
        if odd_seen:
            return all_counts +1
        else:
            return all_counts


