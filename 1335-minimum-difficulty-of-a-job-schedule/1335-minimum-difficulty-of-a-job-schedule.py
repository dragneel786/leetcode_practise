class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        
        def min_difficulty(idx, remain_d):
            # Base Case
            if(remain_d == 1):
                return max(jobDifficulty[idx:])
            
            key = (idx, remain_d)
            if(key in memo):
                return memo[key]
            
            # Recurrence Relation
            ret = inf
            maxv = -inf
            for i in range(idx, n - 1):
                maxv = max(maxv, jobDifficulty[i])
                ret = min(ret, min_difficulty\
                          (i + 1, remain_d - 1) + maxv)
            
            memo[key] = ret
            return ret
            
        n = len(jobDifficulty)
        memo = dict()
        return -1 if(n < d) else min_difficulty(0, d)