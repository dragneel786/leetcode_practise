class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        hash_set = Counter()
        sums = 0
        for num in nums:
            if(hash_set[num] == 0):
                sums += num
            
            elif(hash_set[num] == 1):
                sums -= num
            
            hash_set[num] += 1
        
        return sums