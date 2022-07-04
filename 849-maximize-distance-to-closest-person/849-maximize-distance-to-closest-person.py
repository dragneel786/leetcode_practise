class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        l = [0] * n
        r = [0] * n
        li, ri = 2*n, 2*n
        for i in range(n):
            if(seats[i]): li = i
            l[i] = li
            
            if(seats[n - i - 1]): ri= (n - i - 1)
            r[n - i - 1] = ri
        
        res = 0
        for i in range(n):
            if(not seats[i]):
                lv, rv = abs(i - l[i]), abs(r[i] - i)
                res = max(res, min(lv, rv))
        return res
            