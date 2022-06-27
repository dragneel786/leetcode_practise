class Leaderboard:

    def __init__(self):
        self.scores = dict()

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] = self.scores.get(playerId, 0) + score

    def top(self, K: int) -> int:
        val = list(self.scores.values())
        heap = val[:K]
        heapify(heap)
        for v in val[K:]:
            if(v > heap[0]):
                heappop(heap)
                heappush(heap, v)
        return sum(heap)

    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)