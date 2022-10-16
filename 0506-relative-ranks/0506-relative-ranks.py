class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        def rank(p):
            if(p == 1):
                return "Gold Medal"
            
            if(p == 2):
                return "Silver Medal"
            
            if(p == 3):
                return "Bronze Medal"
            
            return str(p)
        
        n = len(score)
        values = [(s, i) for i, s in enumerate(score)]
        values.sort(reverse=True)
        res = [""] * n
        
        for i, (_, idx) in enumerate(values):
            res[idx] = rank(i + 1)
        
        return res
            
            