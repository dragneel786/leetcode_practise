class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = (10 ** 9) + 7
        scount = ps = 0
        ans = 1
        ss = 0
        for c in corridor:
            scount += c == 'S'
            ss += c == 'S'
            if(scount == 2):
                ps += c == 'P'
            
            if(scount > 2):
                ans= (ans * (ps + 1)) % MOD
                ps = 0
                scount = 1
            
        return ans if(ss >= 2 and ss % 2 == 0) else 0
        
        
    