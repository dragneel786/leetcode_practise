class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if(n < 3):
            return []

        nums.sort()
        res = []
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            while(j < k):
                val = nums[i] + nums[j] + nums[k]
                if(val == 0):
                    arr = [nums[i], nums[j], nums[k]]
                    if(arr not in res):
                        res.append(arr)
                    j += 1
                    k -= 1

                elif(val < 0):
                    j += 1

                else:
                    k -= 1


        return res