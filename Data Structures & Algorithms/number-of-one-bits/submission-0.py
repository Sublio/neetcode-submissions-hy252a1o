class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_n = bin(n)[2:]
        from collections import Counter
        return Counter(bin_n)["1"]
        