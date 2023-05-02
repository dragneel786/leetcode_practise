class Solution:
    def arraySign(self, nums: List[int]) -> int:
        def remove(v):
            nonlocal zero
            if(v < 0):
                return True
            
            if(v == 0):
                zero = True
            return False
        
        zero = False
        remain = list(filter(remove, nums))
        return 0 if(zero) else (-1 if(len(remain) % 2) else 1)