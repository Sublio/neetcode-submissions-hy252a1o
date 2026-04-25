class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        pointer = 0
        for i in range(len(strs[0])):
            cur_char = strs[0][pointer]
            for j in range(1, len(strs)):
                if pointer >= len(strs[j]) or strs[j][pointer] != cur_char:
                    return res
            res = res + cur_char
            pointer +=1

        return res
        