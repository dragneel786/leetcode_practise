class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m, mtot = len(rolls), sum(rolls)
        mntot = mean * (n + m)
        ntot = mntot - mtot
        print(ntot)
        if ntot < n or ntot / n > 6:
            return []
        
        res = [ntot // n for _ in range(n)]
        ntot -= (n * res[0])
        for i in range(n):
            if res[i] + ntot <= 6:
                res[i] += ntot
                break
            
            else:
                ntot -= (6 - res[i])
                res[i] = 6
        
        return res
        