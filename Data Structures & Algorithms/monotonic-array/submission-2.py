class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        is_increasing, is_decreasing = True, True
        for i in range(1, len(nums)):
            prev, cur = nums[i-1], nums[i]
            if cur > prev:
                is_decreasing = False
            if cur < prev:
                is_increasing = False

        return is_increasing or is_decreasing

