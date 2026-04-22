class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []

        for i in range(len(words)):
            cur_word = words[i]

            for w in words:
                if w != cur_word and len(cur_word) <= len(w) and cur_word in w:
                    res.append(cur_word)
                    break


        return res
        