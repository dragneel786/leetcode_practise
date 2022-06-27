class Leaderboard:

    def __init__(self):
        self.S = Counter()

    def addScore(self, playerId: int, score: int) -> None:
        self.S[playerId] += score

    def top(self, K: int) -> int:
        return sum([v[1] for v in self.S.most_common(K)])

    def reset(self, playerId: int) -> None:
        self.S[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)