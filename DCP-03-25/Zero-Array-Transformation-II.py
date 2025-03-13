class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def isZeroArray(till) -> bool:
            nonlocal nums
            n = len(nums)
            diff_array = [0] * (n + 1)
            for a, b, c in queries[:till]:
                diff_array[a] += c
                diff_array[b + 1] -= c

            tot_sum = 0
            for i in range(n):
                tot_sum += diff_array[i]
                if tot_sum < nums[i]:
                    return False

            return True

        left, right = 0, len(queries)
        if not isZeroArray(right):
            return -1
        
        while(left <= right):
            middle = left + (right - left) // 2
            if isZeroArray(middle):
                right = middle - 1
            else:
                left = middle + 1

        return left