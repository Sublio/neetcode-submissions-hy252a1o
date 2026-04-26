class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct_seen = []
        cnt = Counter(arr)
        for i,v in cnt.items():
            if v == 1 and i not in distinct_seen:
                distinct_seen.append(i)
        return distinct_seen[k-1] if len(distinct_seen) >  k-1 else ""
        
        