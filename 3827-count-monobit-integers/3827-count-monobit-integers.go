func countMonobit(n int) int {
    counts := 0
    for i := range n + 1 {
        if isSingleBits(i) {
            counts++
        }
    }
    return counts
}

func isSingleBits(val int) bool {
    firstBit := (val & 1)
    val >>= 1
    for val > 0 {
        if firstBit != (val & 1) {
            return false
        }
        val >>= 1
    }
    return true
}
