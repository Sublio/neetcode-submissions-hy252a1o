import heapq

class Leaderboard:

    def __init__(self):
        self.scores = {}  # playerId -> score

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] = self.scores.get(playerId, 0) + score

    def top(self, K: int) -> int:
        # Get all positive scores
        all_scores = [s for s in self.scores.values() if s > 0]
        # Get top K
        top_scores = heapq.nlargest(K, all_scores)
        return sum(top_scores)

    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0