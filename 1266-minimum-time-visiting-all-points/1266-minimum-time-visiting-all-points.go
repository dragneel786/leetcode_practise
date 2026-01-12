func minTimeToVisitAllPoints(points [][]int) int {
    res := 0
    for i := 1; i < len(points); i++ {
        dx := abs(points[i - 1][0] - points[i][0])
        dy := abs(points[i - 1][1] - points[i][1])
        res += dx
        if dx < dy {
            res += (dy - dx)
        }
    }
    return res
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}