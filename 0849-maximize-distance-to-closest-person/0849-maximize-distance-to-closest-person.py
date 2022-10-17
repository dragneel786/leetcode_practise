class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        last, res = -1, -inf
        for i, s in enumerate(seats):
            if(s):
                res = max(res, i if(last == -1) else ((i - last) // 2))
                last = i
        
        if(not seats[-1]):
            res = max(res, len(seats) - last - 1)
        return res