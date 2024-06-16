func minPatches(nums []int, n int) int {
    var i, upto, patch = 0, 0, 0
    for upto < n {
        if i < len(nums) && nums[i] <= upto + 1 {
            upto += nums[i]
            i++
        } else {
            upto += (upto + 1)
            patch++
        }
    }
    return patch
}