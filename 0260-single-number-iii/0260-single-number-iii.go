func singleNumber(nums []int) []int {
    var xored = 0
    for _, num := range nums {
        xored ^= num
    }
    
    xored &= -xored
    var val1, val2 = 0, 0
    for _, num := range nums {
        if xored & num > 0{
            val1 ^= num
        } else {
            val2 ^= num
        }
    }
    
    return []int{val1, val2}
}