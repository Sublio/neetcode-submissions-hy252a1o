class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []

        cnt = Counter(nums)
        for k,v in cnt.items():
            if v > len(nums)/3:
                res.append(k)
        return res
        