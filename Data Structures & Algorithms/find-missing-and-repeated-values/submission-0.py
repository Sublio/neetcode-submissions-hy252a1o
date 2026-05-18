class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        max_size = len(grid) ** 2
        seen = set()
        res = [0, 0]
        for row in grid:
            for val in row:
                if val in seen:
                    res[0] = val
                seen.add(val)
        for i in range(1, max_size + 1):
            if i not in seen:
                res[1] = i
        return res