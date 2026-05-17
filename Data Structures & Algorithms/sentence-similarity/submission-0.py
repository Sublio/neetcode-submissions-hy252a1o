class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        similar_set = set()
        for a, b in similarPairs:
            similar_set.add((a, b))
            similar_set.add((b, a))
        
        for w1, w2 in zip(sentence1, sentence2):
            if w1 == w2:
                continue
            if (w1, w2) not in similar_set:
                return False
        
        return True
         
        