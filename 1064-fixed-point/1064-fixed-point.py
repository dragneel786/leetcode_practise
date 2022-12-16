class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        for a, i in enumerate(arr):
            if(a == i):
                return i
        
        return -1