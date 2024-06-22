func numberOfSubarrays(nums []int, k int) int {
    var oddCounts = make(map[int]int)
    oddCounts[0] = 1
    var currCounts, res = 0, 0
    for _, num := range nums {
        if num % 2 == 1 {
            currCounts++
        }
        oddCounts[currCounts]++
        if oddCounts[currCounts - k] > 0 {
            res += oddCounts[currCounts - k]
        }
    }
    
    return res
}