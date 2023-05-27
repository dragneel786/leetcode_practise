class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        @lru_cache(None)
        def winner(alice, i):
            if(i >= len(stoneValue)):
                return 0
            
            tot = 0
            res = -inf if(alice) else inf
            for j in range(1, 4):
                if(i + j > len(stoneValue)):
                    break
                
                tot += stoneValue[i + j - 1]
                val = winner(not alice, i + j)
                if(alice):
                    res = max(tot + val, res)
                else:
                    res = min(val, res)
            
            return res
        
        ret = winner(True, 0)
        bob_val = sum(stoneValue) - ret
        print(ret)
        return "Tie" if(ret==bob_val) else 'Alice' if(ret > bob_val) else "Bob"