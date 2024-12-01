class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        vals = {a:i for i,a in enumerate(arr)}
        for i, a in enumerate(arr):
            mv = a // 2
            if a % 2 == 0 and\
            mv in vals and\
            vals[mv] != i:
                return True
        
        return False