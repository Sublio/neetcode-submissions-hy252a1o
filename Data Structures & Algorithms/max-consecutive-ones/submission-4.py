class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) == 1 and nums[0] == 1:
            return 1
        max_seen = 1 if nums[0] == 1 else 0

        for i in range(0, len(nums)):
            cur_seen = 0
            if nums[i] == 1 and (i == 0 or nums[i-1] != 1):
                cur_seen = 1
                for j in range(i+1, len(nums)):
                    if nums[j] == 1:
                        cur_seen +=1
                    else:
                        break
            max_seen = max(max_seen, cur_seen)
                    

        return max_seen
