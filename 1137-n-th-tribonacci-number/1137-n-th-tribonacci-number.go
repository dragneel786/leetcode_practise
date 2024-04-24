func tribonacci(n int) int {
    t0, t1, t2 := 0, 1, 1
    for range n {
        t0, t1, t2 = t1, t2, t0 + t1 + t2
    }
    return t0
}