func rotateString(s string, goal string) bool {
    n := len(s)
    for i := range s {
        if s[i:n] + s[:i] == goal {
            return true
        }
    }
    return false
}