class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        
        def is_prime(val):
            for div in range(2, int(sqrt(val)) + 1):
                if(val % div == 0):
                    return False
            
            return val != 1 and True
                
        n = len(nums)
        max_val = 0
        
        for i in range(n):
            if is_prime(nums[i][i]):
                max_val = max(max_val, nums[i][i])
        
        for i in range(n):
            if is_prime(nums[i][n-i-1]):
                max_val = max(max_val, nums[i][n - i - 1])
        
        return max_val