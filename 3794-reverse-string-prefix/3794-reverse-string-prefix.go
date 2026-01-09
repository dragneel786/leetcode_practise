func reversePrefix(s string, k int) string {
    var first, second []rune
    for i, c := range s {
        if i >= k {
            second = append(second, c)
        } else {
            first = append(first, c)
        }
    }

    slices.Reverse(first)
    return string(first) + string(second)
}