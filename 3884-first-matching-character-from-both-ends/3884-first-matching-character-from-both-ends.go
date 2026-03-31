func firstMatchingIndex(s string) int {
    start, end := 0, len(s) - 1
    for start <= end {
        if s[start] == s[end] {
            return start
        }
        start++
        end--
    }
    return -1
}