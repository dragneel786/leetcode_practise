class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        @lru_cache(None)
        def schedule(idx):
            if(idx >= len(jobs)):
                return 0

            new_i = bisect_left(starts, jobs[idx][1])
            return max(schedule(idx + 1), jobs[idx][2] + schedule(new_i))

        jobs = sorted(zip(startTime, endTime, profit))
        starts = [s[0] for s in jobs]
        return schedule(0)