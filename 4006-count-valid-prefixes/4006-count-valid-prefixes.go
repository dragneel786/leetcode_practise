func countValidPrefixes(s string) int {
    zeros, ones, res := 0, 0, 0
    for _, c := range s {
        if c == '0' {
            zeros++
        } else {
            ones++
        }
        diff := zeros - ones
        if slices.Contains([]int{-1, 0, 1}, diff) {
            res++
        }
    }

    return res
}