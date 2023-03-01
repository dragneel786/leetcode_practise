class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if(len(nums) > 1):
            pivot = random.choice(nums)
            left, right, eq = [], [], []
            for num in nums:
                if(num > pivot):
                    right.append(num)
                elif(num < pivot):
                    left.append(num)
                else:
                    eq.append(num)

            return self.sortArray(left) + eq + self.sortArray(right)
        
        return nums
            