class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1, len(arr)):
            arr[i] ^= arr[i - 1]
        
        # print(arr)
        res = []
        for a, b in queries:
            ans = arr[b]
            if(a > 0):
                ans ^= arr[a - 1]
        
            res.append(ans)
        
        return res
        