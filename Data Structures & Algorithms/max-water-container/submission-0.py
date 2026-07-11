class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        max_seen = 0

        while l < r:
            cur_water_amount = (r-l) * min(heights[l], heights[r])
            max_seen = max(max_seen, cur_water_amount)
            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1
        
        return max_seen

        