func constructTransformedArray(nums []int) []int {
    n := len(nums)
    res := make([]int, n)
    for i, val := range nums {
        index := (((i + val) % n) + n) % n
        res[i] = nums[index]
    }
    return res
}