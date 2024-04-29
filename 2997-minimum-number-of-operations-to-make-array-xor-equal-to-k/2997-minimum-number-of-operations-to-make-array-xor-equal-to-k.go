func minOperations(nums []int, k int) int {
    numsXor := 0
    for _, num := range nums {
        numsXor ^= num
    }
    
    changes := 0
    for k != 0 || numsXor != 0 {
        if k & 1 != numsXor & 1 {
            changes++
        }
        
        if k > 0 { k >>= 1}
        if numsXor > 0 { numsXor >>= 1}
    }
    return changes
}