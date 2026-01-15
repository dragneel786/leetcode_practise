func maxLen(Bars []int) int {
    count,length := 2,2;
    for i := 1; i < len(Bars); i++ {
        if Bars[i] - Bars[i-1] == 1 { count++
        } else {count = 2}
        length = max(length, count)
    }
    return length
}
func maximizeSquareHoleArea(n int, m int, hBars []int, vBars []int) int {
    sort.Ints(hBars)
    sort.Ints(vBars)
    side := min(maxLen(hBars), maxLen(vBars))
    return side * side
}