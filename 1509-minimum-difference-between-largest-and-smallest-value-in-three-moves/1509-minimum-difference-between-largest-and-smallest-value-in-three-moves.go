func minDifference(nums []int) int {
    var size = len(nums)
    if size < 5 { return 0 }
    slices.Sort(nums)
    return min(nums[size - 4] - nums[0], nums[size - 3] - nums[1],
               nums[size - 2] - nums[2], nums[size - 1] - nums[3])
}