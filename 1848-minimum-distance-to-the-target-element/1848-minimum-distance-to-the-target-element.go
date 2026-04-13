func getMinDistance(nums []int, target int, start int) int {
    res := 100_000
    for i, num := range nums {
        if num == target {
            if abs(i - start) < res {
                res = abs(i - start)
            }
        }
    }
    return res
}

func abs(diff int) int {
    if diff < 0 {
        return -1 * diff
    }
    return diff
}