class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        max_value = len(nums)
        res = []

        for i in range(1,max_value+1):
            if i not in nums:
                res.append(i)
        return res
        