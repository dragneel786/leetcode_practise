class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_small = second_small = inf
        for num in nums:
            if(first_small > num):
                first_small = num
            elif(first_small != num and second_small > num):
                second_small = num
            elif(second_small < num):
                return True
        return False