class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        
        m, n = len(people), len(req_skills)
        skill_idx = {v:i for i, v in enumerate(req_skills)}
        dp = {0:[]}
        for i, skills in enumerate(people):
            skill_mask = 0
            for skill in skills:
                skill_mask = skill_mask | (1 << skill_idx[skill])
            
            for curr_mask, need in list(dp.items()):
                comb = curr_mask | skill_mask
                if(comb == curr_mask):
                    continue
                
                if(comb not in dp or len(dp[comb]) > len(need) + 1):
                    dp[comb] = need + [i]
            
            
        return dp[(1 << n) - 1]