class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        init_number = ""
        for d in digits:
            init_number = init_number + str(d)
        new_number = str(int(init_number) + 1)
        for c in new_number:
            res.append(int(c))
        return res
        