class Solution:
    def removeVowels(self, s: str) -> str:
        vovels = "aeiou"
        res = ""
        for c in s:
            if c not in vovels:
                res = res + c
        return res