class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        @lru_cache(None)
        def job_schedule(curr, remain_d):
            if (curr >= len(jobDifficulty)):
                return inf if (remain_d != 0) else 0

            if (remain_d <= 0):
                return inf

            ret = inf
            max_job = 0
            for idx in range(curr, len(jobDifficulty) + 1 - remain_d):
                max_job = max(max_job, jobDifficulty[idx])
                ret = min(ret, max_job + job_schedule(idx + 1, remain_d - 1))

            return ret
            
        ret = job_schedule(0, d)
        return ret if(ret != inf) else -1