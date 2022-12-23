class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxv = -1
        for i in range(len(arr) - 1, -1, -1):
            tmax = max(maxv, arr[i])
            arr[i] = maxv
            maxv = tmax
        
        return arr
            
        