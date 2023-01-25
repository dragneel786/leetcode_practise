class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        n = len(arr)
        tot = sum(arr)
        sums = 0
        parts = 0
        for i in range(n):
            sums += arr[i]
            if(sums == tot / 3):
                parts += 1
                sums = 0
                
        return parts >= 3
            
        
                