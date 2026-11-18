class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        min_num = min(nums)
        res = 0

        while min_num:
            res += min_num%10
            min_num //=10
        return 1 if res %2 ==0 else 0
