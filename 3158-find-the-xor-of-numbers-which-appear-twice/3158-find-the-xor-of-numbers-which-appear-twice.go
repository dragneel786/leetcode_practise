func duplicateNumbersXOR(nums []int) int {
    var numsCount = make(map[int]int)
    for _, num := range nums {
        numsCount[num]++
    }
    
    var xor = 0
    for key, value := range numsCount {
        if value == 2 {
            xor ^= key
        }
    }
    
    return xor
}