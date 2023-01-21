class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        nums.sort()
        nums.append(inf)
        maxvc = [0, -1]
        count = 1
        for i in range(1, len(nums)):
            if(nums[i - 1] != nums[i]):
                if(nums[i - 1] % 2 == 0):
                    if(maxvc[0] < count):
                        maxvc = [count, nums[i - 1]]
                count = 0      
            count += 1
            
        return maxvc[1]
                
            