class Solution:
    def isDecomposable(self, s: str) -> bool:
        length_2_block = 0

        pointer_1 = 1
        cur_group_len = 1
        while pointer_1 <= len(s)-1:
            prev_char, cur_char = s[pointer_1-1], s[pointer_1]
            if prev_char == cur_char:
                cur_group_len +=1
            else:
                if cur_group_len % 3 == 1:
                    return False
                if cur_group_len % 3 == 2:
                    length_2_block += 1
                cur_group_len = 1
            pointer_1 +=1
        if cur_group_len % 3 == 1:
            return False
        if cur_group_len % 3 == 2:
            length_2_block += 1
        return length_2_block == 1
