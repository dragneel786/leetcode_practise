func bitwiseComplement(n int) int {
    if n == 0 {
        return 1
    }

    inc, val := 1, 0
    for inc < n {
        val = val | (inc ^ (n & inc))
        inc <<= 1
    }
    return val
}