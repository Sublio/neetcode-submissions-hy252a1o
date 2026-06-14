class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        source_set = set(source)
        for ch in target:
            if ch not in source_set:
                return -1
        
        count = 1
        i = 0
        
        for ch in target:
            while i < len(source) and source[i] != ch:
                i += 1
            
            if i == len(source):
                count += 1
                i = 0
                while i < len(source) and source[i] != ch:
                    i += 1
            
            i += 1
        
        return count