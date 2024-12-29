class Solution:
    def numWays(self, words: List[str], target: str) -> int:

        @lru_cache(None)
        def get_ways(i, k):
            nonlocal MOD
            if (len(words[0]) - k) < (len(target) - i):
                return 0
            
            if i >= len(target):
                return 1
            
            mul = word_counts[k][target[i]]
            return (get_ways(i, k + 1) + (mul * get_ways(i + 1, k + 1))) % MOD
            
        MOD = (10 ** 9) + 7
        m, n = len(words[0]), len(target)
        word_counts = [Counter() for _ in range(m)]
        for word in words:
            for i, c in enumerate(word):
                word_counts[i][c] += 1

        return get_ways(0, 0) % MOD