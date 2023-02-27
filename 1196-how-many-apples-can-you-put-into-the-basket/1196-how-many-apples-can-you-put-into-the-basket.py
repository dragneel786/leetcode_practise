class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        cap = 5000
        weight.sort()
        c = 0
        for w in weight:
            if(cap < w):
                break
            cap -= w
            c += 1
        
        return c