class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(l, r):
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        
        n = len(s)
        reverse(0, n - 1)
        
        start = 0
        for i in range(n + 1):
            if i == n or s[i] == ' ':
                reverse(start, i - 1)
                start = i + 1
        