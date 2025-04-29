class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        idx_map = defaultdict(list)
        for i, card in enumerate(cards):
            idx_map[card].append(i)
        
        res = inf
        for values in idx_map.values():
            for i in range(1, len(values)):
                res = min(res, values[i] - values[i - 1] + 1)

        return -1 if res == inf else res

