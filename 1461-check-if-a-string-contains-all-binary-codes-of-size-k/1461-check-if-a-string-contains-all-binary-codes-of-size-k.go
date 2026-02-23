func hasAllCodes(s string, k int) bool {
    exists := struct{}{}
    bin_set := make(map[string]struct{})
    for i := k; i <= len(s); i++ {
        bin_set[s[i - k: i]] = exists
    }
    fmt.Print(bin_set)
    return len(bin_set) == int(math.Pow(2, float64(k)))
}