class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        s_pointer, t_pointer = 0,0

        while t_pointer<len(t) and s_pointer < len(s):
            cur_s_char = s[s_pointer]
            if s[s_pointer] == t[t_pointer]:
                s_pointer +=1
            t_pointer +=1
        return s_pointer == len(s)
        