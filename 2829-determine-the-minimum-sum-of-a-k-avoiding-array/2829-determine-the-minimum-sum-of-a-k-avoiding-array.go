func minimumSum(n int, k int) int {
    var skip = make(map[int]bool)
    var sums, size, curr = 0, 0, 1
    for size < n {
        sums += curr
		skip[k - curr] = true
		size++; curr++;

        for skip[curr] {
            curr++
        }
    }
    return sums
}