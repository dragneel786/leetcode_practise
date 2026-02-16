func reverseBits(n int) int {
    res := 0
    for i := range 32 {
        res <<= 1
        if (n & (1 << i)) != 0 {
            res |= 1
        }
    }
    return res
}