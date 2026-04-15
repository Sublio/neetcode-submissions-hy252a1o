class Solution:
    def confusingNumber(self, n: int) -> bool:
        orig = n
        mapping = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        rotated = 0
        invalid_nums = [2, 3, 4, 5, 7]
        while n > 0:
            cur_last_n = n % 10
            if cur_last_n in invalid_nums:
                return False
            rotated = rotated * 10 + mapping[cur_last_n]
            n = n // 10
        return rotated != orig