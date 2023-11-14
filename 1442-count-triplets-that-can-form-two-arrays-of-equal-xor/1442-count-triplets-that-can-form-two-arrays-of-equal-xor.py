class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        for i in range(n):
            pre = arr[i]
            for j in range(i + 1, n):
                pre ^= arr[j]
                res += (j - i) if(pre == 0) else 0
        
        return res