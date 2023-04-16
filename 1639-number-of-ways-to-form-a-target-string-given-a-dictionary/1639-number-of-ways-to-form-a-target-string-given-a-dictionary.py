class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        
        def create_imap():
            col_map = defaultdict(Counter)
            for word in words:
                for i, c in enumerate(word):
                    col_map[i][c] += 1
            
            return col_map
        
        @lru_cache(None)
        def num_ways(i, j):
            nonlocal m, n, MOD
            if(j >= n):
                return 1
            
            if(i >= m):
                return 0
            
            return (num_ways(i + 1, j) +\
                    (column_map[i][target[j]] * \
                    num_ways(i + 1, j + 1))) % MOD
            
                
        MOD = 10 ** 9 + 7
        m, n = len(words[0]), len(target)
        column_map = create_imap()
        return num_ways(0, 0)