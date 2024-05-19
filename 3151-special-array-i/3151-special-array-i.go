func isArraySpecial(nums []int) bool {
    var isEven = nums[0] & 1
    for i := range len(nums) - 1 {
        var isCurrentNumEven = nums[i + 1] & 1
        if isEven == isCurrentNumEven {
            return false
        }
        isEven = isCurrentNumEven
    }
    return true
}