func minPartitions(n string) int {
    maxVal := 0
    for _, c := range n {
        maxVal = max(maxVal, int(c - '0'))
    }

    return maxVal
}

func max(a, b int) int {
    if (a < b) {
        return b
    }
    return a
}