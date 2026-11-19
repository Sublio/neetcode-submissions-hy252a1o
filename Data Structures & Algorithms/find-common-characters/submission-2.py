class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        import string
        alphabet = string.ascii_lowercase
        res = []
        for c in alphabet:
            cur_char_counters = []
            for word in words:
                if c in word:
                    word_cnt = Counter(word)[c]
                    cur_char_counters.append(word_cnt)
                else:
                    cur_char_counters = []
                    break
            if cur_char_counters:
                res.extend(min(cur_char_counters)*c)

        return res
        