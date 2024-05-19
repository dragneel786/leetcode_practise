func maximumValueSum(nums []int, k int, edges [][]int) int64 {
    var bestSum, counts = 0, 0
    var minDiff = math.MaxInt
    for _, num := range nums {
        var xorNum = num ^ k
        minDiff = min(minDiff, int(math.Abs(float64(num - xorNum))))
        if xorNum > num {
            bestSum += xorNum
            counts++
        } else {
            bestSum += num
        }
    }
    
    if counts % 2 == 1 {
        bestSum -= minDiff
    }
    return int64(bestSum)
}