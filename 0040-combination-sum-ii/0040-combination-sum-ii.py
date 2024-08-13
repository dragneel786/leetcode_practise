class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def combo(i, tot, cbs = []):
            if i >= len(candidates) or tot >= target:
                if tot == target:
                    res.append(cbs.copy())
                    
                return
            
            combo(i + 1, tot + candidates[i], cbs + [candidates[i]])
            i += 1
            while(i < len(candidates) and candidates[i - 1] == candidates[i]):
                i += 1
            combo(i, tot, cbs)
            return 
        
        res = []
        candidates.sort()
        candidates.append(51)
        combo(0, 0)
        return res
        