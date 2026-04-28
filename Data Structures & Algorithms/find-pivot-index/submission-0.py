class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            left, right = nums[:i], nums[i+1:]
            if sum(left) == sum(right):
                return i
        return -1

        