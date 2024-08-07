class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        wins = defaultdict(Counter)
        for x, y in pick:
            wins[x][y] += 1
        
        res = 0
        print(wins)
        for key, counts in wins.items():
            for c in counts.values():
                if c > key:
                    res += 1
                    break
            
        return res