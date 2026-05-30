class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        if not arrays:
            return 0
        
        m = len(arrays)
        min_val, min_idx = float('inf'), -1
        max_val, max_idx = float('-inf'), -1
        
        for i, arr in enumerate(arrays):
            if arr[0] < min_val:
                min_val = arr[0]
                min_idx = i
            if arr[-1] > max_val:
                max_val = arr[-1]
                max_idx = i
        
        if min_idx != max_idx:
            return max_val - min_val
        
        second_max_val = float('-inf')
        second_min_val = float('inf')
        
        for i, arr in enumerate(arrays):
            if i != max_idx:
                second_max_val = max(second_max_val, arr[-1])
            if i != min_idx:
                second_min_val = min(second_min_val, arr[0])
        
        return max(max_val - second_min_val, second_max_val - min_val)
        