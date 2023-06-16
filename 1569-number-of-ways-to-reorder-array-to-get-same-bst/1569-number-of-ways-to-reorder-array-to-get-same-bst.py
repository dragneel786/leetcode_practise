class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        
        MOD = 10 ** 9 + 7 
        def ways(arr):
            if(len(arr) <= 2):
                return 1
            
            left = []
            right = []
            for a in arr:
                if a > arr[0]:
                    right.append(a)
                
                if(a < arr[0]):
                    left.append(a)
                    
            a = len(left)
            b = len(right)
            return ways(left) * ways(right) * comb(a+b, a)
    
        return (ways(nums) - 1) % MOD