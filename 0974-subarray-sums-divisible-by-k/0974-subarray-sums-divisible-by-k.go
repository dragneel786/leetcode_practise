func subarraysDivByK(nums []int, k int) int {
    var modOccur = make(map[int]int)
    var currSum, counts = 0, 0

    modOccur[0] = 1
    for _, num := range nums {
        currSum = (currSum + num % k + k) % k
        // var mod = int(math.Abs(float64()))
        fmt.Println(currSum)
        counts += modOccur[currSum]
        modOccur[currSum]++
    }
    return counts
}