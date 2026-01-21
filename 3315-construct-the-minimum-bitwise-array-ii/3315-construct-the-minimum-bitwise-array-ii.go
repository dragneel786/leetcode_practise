
func minBitwiseArray(values []int) []int {
    n := len(values)
    result := make([]int, n)

    for i := 0; i < n; i++ {
        cur := values[i]

        if cur == 2 {
            result[i] = -1
            continue
        }

        temp := cur
        cnt := 0

        for (temp & 1) == 1 {
            cnt++
            temp >>= 1
        }

        result[i] = cur - (1 << (cnt - 1))
    }

    return result
}