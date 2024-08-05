func doesAliceWin(s string) bool {
    for _, c := range s {
        var ch = byte(c)
        if ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' {
            return true
        }
    }
    return false
}