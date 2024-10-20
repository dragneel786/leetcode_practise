class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        def combos(val = [], idx = 0):
            nonlocal nums, k, n
            if len(val) > k or sum(val) > n:
                return
            
            if len(val) == k and sum(val) == n:
                res.append(val[:])
                return
            
            for i in range(idx, 9):
                combos(val + [nums[i]], i + 1)
                
        
        nums = [1,2,3,4,5,6,7,8,9]
        res = [] 
        combos()
        return res
    