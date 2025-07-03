class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        def is_prime(num):
            for v in range(2, floor(sqrt(num)) + 1):
                if num % v == 0:
                    return False
            return num != 1
        
        for val in Counter(nums).values():
            if is_prime(val):
                return True
        
        return False