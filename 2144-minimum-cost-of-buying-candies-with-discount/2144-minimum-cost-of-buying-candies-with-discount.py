class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        # cost.sort(
        return sum([a for i, a in enumerate(sorted(cost)[::-1])
                    if((i + 1) % 3)])