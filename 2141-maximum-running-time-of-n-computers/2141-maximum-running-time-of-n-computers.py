class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        
        def calcy(hrs):
            i = m - 1
            while(i and batteries[i] >= hrs):
                i -= 1
            
            remain = n - (m - i - 1)
            return sum(batteries[:i + 1]) >= remain * hrs
            
        m = len(batteries)
        batteries.sort()
        low = batteries[0]
        high = sum(batteries)
        ans = 0
        while(low <= high):
            mid = (high - low) // 2 + low
            ret = calcy(mid)
            if(ret):
                low = mid + 1
                ans = mid
            else:
                high = mid - 1
                
        return ans
            
            
    