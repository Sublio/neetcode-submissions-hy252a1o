class Solution:
    def longestConsecutive(self, nums) -> int:
        if not nums: return 0
        num_set = set(nums)
        min_seen = {}
        for cur_num in num_set:
            if cur_num - 1 not in num_set:
                cur_sequence = 1
                prev_num = cur_num
                while prev_num + 1 in num_set:
                    cur_sequence += 1
                    prev_num += 1
                min_seen[cur_num] = cur_sequence
        return max(min_seen.values())