class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        r = []
        for i in range(n - 1, -1, -1):
            if(seats[i]):
                r.append(i)
            
        res = 0
        lt = 2*n
        rt = 2*n if(not r) else r.pop()
        for i in range(n):
            if(i > rt):
                rt = 2*n if(not r) else r.pop()
                
            if(not seats[i]):
                lv, rv = abs(lt - i), abs(i - rt)
                res = max(res, min(lv, rv))
            else:
                lt = i
                
        return res
            