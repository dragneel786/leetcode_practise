class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if(n < m * k):
            return -1

        low = 1
        high = max(bloomDay)

        def canMake(mid):
            made = 0
            f = 0
            for i in range(n):
                if(bloomDay[i] <= mid):
                    f += 1
                else:
                    f = 0 
                if(f == k):
                    made += 1
                    f = 0

            return made >= m


        res = 0
        while(low <= high):
            mid = (high -  low) // 2 + low
            if(canMake(mid)):
                high = mid - 1
                res = mid
            else:
                low = mid + 1

        return res