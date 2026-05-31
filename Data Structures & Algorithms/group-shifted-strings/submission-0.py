class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def normalize(s):
            shift = (26 - (ord(s[0]) - ord('a'))) % 26
            return ''.join(chr((ord(c) - ord('a') + shift) % 26 + ord('a')) for c in s)
        
        groups = defaultdict(list)
        for s in strings:
            groups[normalize(s)].append(s)
        
        return list(groups.values())
        