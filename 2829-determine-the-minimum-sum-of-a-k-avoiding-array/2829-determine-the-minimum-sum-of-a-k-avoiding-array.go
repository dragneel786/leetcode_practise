func minimumSum(n int, k int) int {
    var exists = make(map[int]bool)
    var sums, size, curr = 0, 0, 1
    for size < n {
        sums += curr
		exists[curr] = true
		size++; curr++;

        for exists[k - curr] {
            curr++
        }
    }
    return sums
}