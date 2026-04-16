class Solution:
    def countElements(self, arr: List[int]) -> int:
        res = []

        for elem in arr:
            if elem +1 in arr:
                res.append(elem)

        return len(res)
        