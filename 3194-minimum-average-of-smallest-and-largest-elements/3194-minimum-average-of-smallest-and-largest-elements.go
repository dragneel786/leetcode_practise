func minimumAverage(nums []int) float64 {
    var res = 100000.0
    slices.Sort(nums)
    for i := 0; i < (len(nums) / 2); i++ {
        res = min(res, float64(nums[i] + nums[len(nums) - i - 1]) / 2)
    }
    
    return res
}