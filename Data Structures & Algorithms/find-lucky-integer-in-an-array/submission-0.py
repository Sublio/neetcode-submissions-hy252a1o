class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res = -1
        seen = []

        cnt = Counter(arr)
        for k,v in cnt.items():
            if k == v:
                seen.append(k)
        return max(seen) if seen else res 
        