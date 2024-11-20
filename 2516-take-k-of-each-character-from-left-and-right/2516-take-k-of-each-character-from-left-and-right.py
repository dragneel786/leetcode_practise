class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        counts = Counter(s)
        for c in ['a', 'b', 'c']:
            if counts[c] < k:
                return -1

        n = len(s)
        start = 0
        res = inf
        for end, c in enumerate(s):
            counts[c] -= 1
            while(start <= end and counts[c] < k):
                counts[s[start]] += 1
                start += 1

            res = min(n - (end - start + 1), res)

        return res
