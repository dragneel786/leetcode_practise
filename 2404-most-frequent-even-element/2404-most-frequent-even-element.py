class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        res = count = -1
        ncount = Counter()
        for num in nums:
            ncount[num] += 1
            if(num % 2 == 0):
                if(ncount[num] > count or\
                   (ncount[num] == count and num < res)):
                    res = num
                    count = ncount[num]
                
        return res
                
            