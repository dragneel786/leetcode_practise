func minOperations(s string) int {
    return min(findRes(s, '1'), findRes(s, '0'))
}

func findRes(s string, ch rune) int {
    res := 0
    for _, c := range s {
        if c != ch {
            res++
        }
        if ch == '0' {
            ch = '1'
        } else { ch = '0' }
    }
    return res
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
