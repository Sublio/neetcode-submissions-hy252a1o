class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            cur_num = nums[i]
            cur_diff = target - nums[i]
            if cur_diff not in seen:
                seen[cur_num] = i
            else:
                return [seen[cur_diff],i]

        