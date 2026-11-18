class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            prev,cur = nums[i-1], nums[i]
            cur_diff = cur - prev
            if cur == prev or cur < prev or cur_diff !=1:
                return False
        return True


