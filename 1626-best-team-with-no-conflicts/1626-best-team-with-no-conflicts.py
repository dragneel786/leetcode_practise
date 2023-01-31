class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        
#         def pick_high(i = 0, pick = -1):
#             if(i >= len(age_score)):
#                 return 0
            
#             key = (i, pick)
#             if(key in memo):
#                 return memo[key]
            
#             if(pick == -1 or age_score[pick][1] <= age_score[i][1]):
#                 memo[key] = age_score[i][1] +\
#                 pick_high(i + 1, i)
            
#             memo[key] = max(memo[key], pick_high(i + 1, pick))
#             return memo[key]
        
        age_score = [(a, s) for a, s in zip(ages, scores)]
        age_score.sort()
       
        n = len(age_score)
        dp = [v for _, v in age_score]
        ans = max(dp)
        for i in range(n):
            for j in range(i):
                if(age_score[i][1] >= age_score[j][1]):
                    dp[i] = max(dp[i], age_score[i][1] + dp[j])
                    ans = max(ans, dp[i])
                
        return ans
            