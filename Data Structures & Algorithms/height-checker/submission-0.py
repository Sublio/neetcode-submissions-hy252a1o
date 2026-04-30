class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        res = 0

        for i in range(len(heights)):
            cur_student = heights[i]
            expected_student = expected[i]
            if cur_student != expected_student:
                res +=1
        return res
        