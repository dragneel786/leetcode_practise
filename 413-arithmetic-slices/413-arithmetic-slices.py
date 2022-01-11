class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if(n < 3):
            return 0
        dp = [float('inf') for _ in range(n)]
        val = nums[0] - nums[1]

        for i in range(2, n):
            temp = nums[i - 1] - nums[i]
            if(val == temp):
                dp[i - 1], dp[i] = temp, temp
            val = temp
            
        length = 2
        count = 0
        for i in range(n - 2):
            newList = [float('inf')] * (n - length + 1)
            for j in range(n - length):
                temp1 = dp[j + 1]
                temp2 = dp[j + 2]
                if(temp1 != float('inf') and temp2 != float('inf') and temp1 == temp2):
                    newList[j + 1] = temp1
                    count += 1
            dp = newList
            length += 1

        return count