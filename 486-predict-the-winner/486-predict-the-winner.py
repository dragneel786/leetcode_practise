class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @functools.lru_cache(None)
        def predict(left, right, player):
            if(left > right):
                return 0
            
            if(not player):
                return max(nums[left] + predict(left + 1, right, 1),\
                           nums[right] + predict(left, right - 1, 1))
            else:
                return min(predict(left + 1, right, 0), predict(left, right - 1, 0))
                 
        n = len(nums)
        val = predict(0, n - 1, 0)
        return val >= (sum(nums) - val)