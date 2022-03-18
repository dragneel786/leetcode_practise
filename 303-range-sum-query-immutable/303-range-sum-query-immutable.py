class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.prefix = [nums[0]] + [0] * (n - 1)
        for i in range(1, n):
            self.prefix[i] = self.prefix[i - 1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if(left == 0):
            return self.prefix[right]
        
        return self.prefix[right] - self.prefix[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)