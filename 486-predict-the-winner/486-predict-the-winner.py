class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def predict(left, right):
            key = (left, right)
            if(left > right):
                return 0
            
            if(key not in memo):
                memo[key] = nums[left] + min(predict(left + 2, right),\
                                             predict(left + 1, right - 1))
                memo[key] = max(memo[key], nums[right] + min(predict(left + 1, right - 1),\
                                             predict(left, right - 2)))
            return memo[key]
                 
        n = len(nums)
        memo = {}
        val = predict(0, n - 1)
        return val >= (sum(nums) - val)