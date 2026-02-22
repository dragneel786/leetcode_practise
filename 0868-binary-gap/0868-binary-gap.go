func binaryGap(n int) int {
    prev, curr := -1, -1
    res, i := 0, 0
    for n > 0 {
        if (n & 1) == 1 {
            prev = curr
            curr = i
            if prev != -1 {
                res = max(res, curr - prev)
            }
        }
        i++
        n >>= 1
    }
    return res
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}