class Solution:
    def firstUniqChar(self, s: str) -> int:
        res = -1

        cnt = Counter(s)

        for k,v in cnt.items():
            if v == 1:
                for i in range(len(s)):
                    if s[i] == k:
                        return i
        return res
