class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        s_len = len(s)
        cnt_s = Counter(s)

        if s_len % 2  == 0:
            for k,v in cnt_s.items():
                if v % 2 == 1:
                    return False
        else:
            seen_one_char = False
            seen_second_char = False
            for k,v in cnt_s.items():
                if v % 2 !=0 and seen_one_char == False:
                    seen_one_char = True
                elif v%2 != 0 and seen_second_char == False:
                    seen_second_char = True
                elif seen_one_char and seen_second_char:
                    return False
        return True


        