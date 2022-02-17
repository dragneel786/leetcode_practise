class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def getCombo(candi, t, op = []):
            if(not t):
                return [op.copy()]

            if(t < 0):
                return []

            res = []
            for i in range(len(candi)):
                temp = getCombo(candi[i:], t - candi[i], op + [candi[i]])
                if(temp):
                    res.extend(temp)

            return res
    
        return getCombo(candidates, target)