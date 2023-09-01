class Solution:
    def countTriples(self, n: int) -> int:
        items = [v ** 2 for v in range(1, n + 1)]
        sq_set = set(items)
        count = 0
        for a, b in combinations(items, 2):
            count += ((a + b) in sq_set) * 2
        return count
            