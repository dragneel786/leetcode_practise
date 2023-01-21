class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        res = count = -1
        for c, num in sorted([(c, n) for n, c in Counter(nums).items()]):
            if(num % 2 == 0):
                if(count < c):
                    res = num
                    count = c
            
        return res
                
            