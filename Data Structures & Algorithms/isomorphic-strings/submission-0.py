class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map_s = {}
        map_t = {}
        
        for cs, ct in zip(s, t):
            if cs in map_s:
                if map_s[cs] != ct:
                    return False
            else:
                if ct in map_t:
                    return False
                map_s[cs] = ct
                map_t[ct] = cs
        return True
        