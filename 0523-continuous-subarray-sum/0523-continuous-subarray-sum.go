func checkSubarraySum(nums []int, k int) bool {
    var modIndex = make(map[int]int)
    modIndex[0] = -1
    var currSum = 0
    for i, num := range nums {
        currSum += num
        if _, ok := modIndex[currSum % k]; ok {
            if i - modIndex[currSum % k] >= 2 {
                return true
            }
        } else {
            modIndex[currSum % k] = i
        }
    }
    
    return false
}