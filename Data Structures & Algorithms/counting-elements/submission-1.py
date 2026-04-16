class Solution:
    def countElements(self, arr: List[int]) -> int:
        res = 0

        for elem in arr:
            if elem +1 in arr:
                res +=1

        return res
        