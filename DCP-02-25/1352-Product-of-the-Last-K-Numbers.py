class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        jobs = sorted(zip(endTime, startTime, profit))
        n = len(jobs)
        dp = [0] * (n + 1)
        for i in range(n):
            end, start, prof = jobs[i]
            index = bisect_right(jobs, start, hi=i, key=lambda x:x[0])
            dp[i + 1] = max(dp[i], prof + dp[index])
            
        return max(dp)
                