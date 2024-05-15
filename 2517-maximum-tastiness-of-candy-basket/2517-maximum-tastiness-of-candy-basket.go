func maximumTastiness(price []int, k int) int {
    slices.Sort(price)
    var low, high = 0, int(math.Pow(10, 9))
    for low < high {
        var mid = low + ((high - low) / 2)
        if check(k, mid, &price) {
            low = mid + 1
        } else {
            high = mid
        }
    }
    return low - 1
}

func check(k, val int, price *[]int) bool {
    var prev, count = (*price)[0], 1
    for i := 1; i < len(*price) && count < k; i++ {
        if (*price)[i] - prev >= val {
            prev = (*price)[i]
            count++
        }
    }
    return count == k
}