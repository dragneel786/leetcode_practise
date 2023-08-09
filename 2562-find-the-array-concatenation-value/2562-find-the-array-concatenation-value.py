class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        nums = deque(nums)
        sums = 0
        while(nums):
            val1 = str(nums.popleft())
            val2 = ''
            if(nums):
                val2 = str(nums.pop())
            
            sums += int(val1 + val2)
        
        return sums