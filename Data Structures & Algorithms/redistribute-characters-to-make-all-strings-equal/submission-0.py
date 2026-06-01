class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        if len(words) == 1:
            return True
        
        char_count = {}
        for word in words:
            for char in word:
                char_count[char] = char_count.get(char, 0) + 1
        
        n = len(words)
        
        for count in char_count.values():
            if count % n != 0:
                return False
        
        return True
        