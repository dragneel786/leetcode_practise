class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.getPossibleSums(candidates, target, res)
        return res
    
    def getPossibleSums(self, candidates, target, res, op = []):
        if(target == 0):
            res.append(op)
            return

        if(target < 0):
            return

        for i in range(len(candidates)):
            self.getPossibleSums(candidates[i: ], target - candidates[i]\
                , res, op + [candidates[i]])