class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_n = bin(n)[2:]
        res = 0
        for b in bin_n:
            if int(b) == 1:
                res+=1

        return res
        