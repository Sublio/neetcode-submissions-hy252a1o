class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = {}
        for c in chars:
            chars_count[c] = chars_count.get(c, 0) + 1
        
        total_length = 0
        
        for word in words:
            word_count = {}
            can_form = True
            
            for c in word:
                word_count[c] = word_count.get(c, 0) + 1
            
            for c, count in word_count.items():
                if count > chars_count.get(c, 0):
                    can_form = False
                    break
            
            if can_form:
                total_length += len(word)
        
        return total_length
        