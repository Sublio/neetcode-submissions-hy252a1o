class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        for i in range(1, len(nums)):
            prev, cur = nums[i-1], nums[i]
            if prev %2 == 0 and cur % 2 == 0:
                return False
            elif prev %2 != 0 and cur %2 !=0:
                return False
        return True
        