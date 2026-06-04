class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num_count = {}
        
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
        
        duplicate = -1
        missing = -1
        
        for i in range(1, n + 1):
            if i not in num_count:
                missing = i
            elif num_count[i] == 2:
                duplicate = i
        
        return [duplicate, missing]
        