func judgeSquareSum(c int) bool {
    var low, high = 0, int(math.Sqrt(float64(c)))
    for low <= high {
        var val = int(math.Pow(float64(low), 2)) +
        int(math.Pow(float64(high), 2))
        if val == c {
            return true
        } else if val < c {
            low += 1
        } else {
            high -= 1
        }
    }
    
    return false
}