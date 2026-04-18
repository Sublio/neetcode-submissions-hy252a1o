class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        nums = Counter(nums)

        res = -1

        for k,v in nums.items():
            if v == 1 and k > res:
                res = k

        return res
        