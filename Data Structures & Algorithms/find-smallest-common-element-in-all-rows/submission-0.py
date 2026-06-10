class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        m = len(mat)
        if m == 0:
            return -1
        
        counter = Counter()
        
        for row in mat:
            for num in set(row): 
                counter[num] += 1
        
        for num in sorted(counter.keys()):
            if counter[num] == m:
                return num
        
        return -1
        