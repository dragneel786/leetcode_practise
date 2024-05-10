func kthSmallestPrimeFraction(arr []int, k int) []int {
    sortedArr := [][]float64{}
    for i, a := range arr {
        for _, b := range arr[i + 1:] {
            af, bf := float64(a), float64(b)
            sortedArr = append(sortedArr, []float64{af/bf, af, bf})
        }
    }
    slices.SortFunc(sortedArr, func(a, b []float64) int {
		if a[0] < b[0] {
            return -1
        }
        if a[0] > b[0] {
            return 1
        }
        return 0
    })
    
    return []int{int(sortedArr[k - 1][1]), int(sortedArr[k - 1][2])}
}
