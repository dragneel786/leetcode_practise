class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ret = []
        for num in nums[::-1]:
            while(num):
                ret.append(num % 10)
                num //= 10
        
        return reversed(ret)
        