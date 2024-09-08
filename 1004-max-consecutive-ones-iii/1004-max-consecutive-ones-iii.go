func longestOnes(nums []int, k int) int {
    var start, res = 0, 0
    for end := range len(nums) {
        if nums[end] == 0 { k-- }
        for k < 0 {
            if nums[start] == 0 {
                k += 1
            }
            start += 1
        }
        
        res = max(res, end - start + 1)
    }
    
    return res
}