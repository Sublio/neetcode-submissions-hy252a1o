class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            prev = flowerbed[i-1] if i > 0 else 0
            nxt = flowerbed[i+1] if i < len(flowerbed)-1 else 0
            cur = flowerbed[i]
            
            if prev == 0 and cur == 0 and nxt == 0:
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
                    
        return n <= 0

        