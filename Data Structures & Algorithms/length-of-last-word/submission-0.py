class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")
        for i in range(len(words)-1, -1,-1):
            cur_word = words[i]
            if len(cur_word) > 0:
                return len(cur_word)



        