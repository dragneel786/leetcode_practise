class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        s = 0
        e = n - 1
        while(s < n - 1 and arr[s] <= arr[s + 1]):
            s += 1
        if(s == n - 1):
            return 0
        
        while(e > 0 and arr[e] >= arr[e - 1]):
            e -= 1
            
        if(e == 0):
            return n - 1
    
        res = min(n - 1 - s, e)
        i = 0
        j = e
        while(i <= s and j < n):
            if(arr[i] <= arr[j]):
                res = min(j - i - 1, res)
                i += 1
            else:
                j += 1
            
        return res
        
        
        