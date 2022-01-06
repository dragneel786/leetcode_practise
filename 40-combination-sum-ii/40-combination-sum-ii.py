class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        candidates = candidates + [51]
        self.getCombination(candidates, target, res)
        return res
    

    def getCombination(self, candidates, target, res, op = []):
        if(not target):
            res.append(op)
            return

        if(target < 0 or candidates[0] > target):
            return

        self.getCombination(candidates[1:], target - candidates[0], res, op + [candidates[0]])
        i = 1
        while(candidates[i - 1] == candidates[i]):
            i += 1
        self.getCombination(candidates[i:], target, res, op)