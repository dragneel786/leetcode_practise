class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        combos = []
        def genCombo(cand, target, op = []):
            if(target < 0 or not cand):
                return
            
            if(target == 0):
                combos.append(op)
                return 
            
            genCombo(cand, target - cand[0], op + [cand[0]])
            genCombo(cand[1:], target, op)
        
        genCombo(candidates, target)
        return combos