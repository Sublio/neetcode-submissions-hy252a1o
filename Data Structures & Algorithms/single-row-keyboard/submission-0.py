class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        pointer = 0 
        score = 0

        for i in range(len(word)):
            cur_character = word[i]
            desire_index = keyboard.index(cur_character)
            move_score = abs(pointer - desire_index)
            score += move_score
            pointer = desire_index

        return score
        