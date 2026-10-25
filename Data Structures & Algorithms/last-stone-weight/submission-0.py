class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort(reverse=True)
            first, second = stones[0], stones[1]
            if first == second:
                stones = stones[2:]
            else:
                new_stone = first - second
                stones = [new_stone] + stones[2:]
        return stones[0] if stones else 0
        