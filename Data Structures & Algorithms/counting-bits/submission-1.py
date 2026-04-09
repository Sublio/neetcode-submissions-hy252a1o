class Solution:
    def countBits(self, n: int) -> List[int]:
        from collections import Counter
        res = []

        for i in range(n+1):
            bin_rep = bin(i)[2:]
            res.append(Counter(bin_rep)["1"])
        return res
        