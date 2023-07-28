class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        def won(left, right):
            if(left > right):
                return 0
            
            key = (left, right)
            if(key not in memo):
                one = nums[left] + min(won(left + 2, right),\
                                       won(left + 1, right-1))
                two = nums[right] + min(won(left + 1, right - 1),\
                                        won(left, right - 2))
                memo[key] = max(one, two)
                
            return memo[key]
        
        memo = dict()
        tot = sum(nums)
        val = won(0, len(nums) - 1)
        return val >= tot - val