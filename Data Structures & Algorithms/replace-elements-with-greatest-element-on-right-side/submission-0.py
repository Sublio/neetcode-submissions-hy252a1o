class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []

        for i in range(len(arr)):
            if i == len(arr)-1:
                res.append(-1)
            else:
                cur_num = arr[i]
                next_biggest = max(arr[i+1:])
                res.append(next_biggest)
        return res
        