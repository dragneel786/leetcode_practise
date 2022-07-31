class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        
        @lru_cache(None)
        def probs(index, target):
            if(target < 0): return 0
            if(index == 0): return target == 0
            
            return (probs(index - 1, target - 1) * prob[index - 1])\
        + (probs(index - 1, target) * (1 - prob[index - 1]))
        
        return probs(len(prob), target)
            
            