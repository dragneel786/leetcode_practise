func findMaxK(nums []int) int {
    negValues := make(map[int]bool)
    for _, num := range nums {
        if num < 0 {
            negValues[num] = true
        }
    }
    
    res := -1
    for _, num := range nums {
        if num > 0 && negValues[-num] {
            res = max(res, num)
        }
    }
    return res
}