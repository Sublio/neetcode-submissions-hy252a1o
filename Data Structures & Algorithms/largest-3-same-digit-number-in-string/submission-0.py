class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_good = ""
        for i in range(len(num) - 2):
            if num[i] == num[i+1] == num[i+2]:
                current = num[i:i+3]
                if current > max_good:
                    max_good = current
        return max_good
        