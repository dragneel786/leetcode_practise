func countOfPairs(n int, x int, y int) []int {
    if x > y {
        return countOfPairs(n, y, x)
    }
    var res = make([]int, n)
    for i := 1; i <= n; i++ {
        for j := 1; j < i; j++ {
            var dis = i - j
            var diff1 = int(math.Abs(float64(j - x)))
            var diff2 = int(math.Abs(float64(y - i)))
            var minDis = min(dis, diff1 + diff2 + 1)
            res[minDis - 1] += 2
        }
    }
    return res
}