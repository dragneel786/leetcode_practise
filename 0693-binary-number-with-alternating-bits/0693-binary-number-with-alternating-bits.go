func hasAlternatingBits(n int) bool {
    prev := (n & 1) ^ 1
    for n > 0 {
        if prev == (n & 1) {
            return false
        }
        prev = (n & 1)
        n >>= 1
    }
    return true
}