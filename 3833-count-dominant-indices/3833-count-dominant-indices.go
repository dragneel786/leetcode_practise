func dominantIndices(nums []int) int {
    n := len(nums)
    doms, value := 0, nums[n - 1]
    for i := n - 2; i > -1; i-- {
        if (value / (n - i - 1)) < nums[i] {
            doms++
        }
        value += nums[i]
    }
    return doms
}