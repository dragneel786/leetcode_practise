class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = []
        
        curr = 1
        while(n):
            if n & 1:
                powers.append(curr)
            
            curr <<= 1
            n >>= 1
        
        res = []
        MOD = (10 ** 9) + 7
        for s, e in queries:
            val = 1
            for i in range(s, e + 1):
                val = (val * powers[i]) % MOD
            res.append(val)
        
        return res

        

            