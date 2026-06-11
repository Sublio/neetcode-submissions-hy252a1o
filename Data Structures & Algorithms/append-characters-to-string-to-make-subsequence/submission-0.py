class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        j = 0
        for ch in s:
            if j < len(t) and ch == t[j]:
                j += 1
        return len(t) - j
        