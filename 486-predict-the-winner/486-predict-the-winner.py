class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def predict(left, right, player):
            key = (left, right, player)
            if(left > right):
                return 0
            
            if(key not in memo):
                if(not player):
                    memo[key] = max(nums[left] + predict(left + 1, right, 1),\
                               nums[right] + predict(left, right - 1, 1))
                else:
                    memo[key] = min(predict(left + 1, right, 0), predict(left, right - 1, 0))
            return memo[key]
                 
        n = len(nums)
        memo = {}
        val = predict(0, n - 1, 0)
        return val >= (sum(nums) - val)