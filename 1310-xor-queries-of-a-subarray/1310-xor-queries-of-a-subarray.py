class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1, len(arr)):
            arr[i] ^= arr[i - 1]
        
        res = []
        for i, j in queries:
            val = arr[j]
            if i > 0:
                val ^= arr[i - 1]
            
            res.append(val)
        
        return res
        