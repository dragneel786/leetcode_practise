func maxProfitAssignment(difficulty []int, profit []int, worker []int) int {
    
    var prodDiff = [][]int{}
    var binSearch = func(value int) int {
        var low, high = 0, len(difficulty) - 1
        for low < high {
            var mid = (low + high + 1) >> 1
            if prodDiff[mid][0] <= value {
                low = mid
            } else {
                high = mid - 1
            }
        }
        return low
    }

    for i := range len(difficulty) {
        prodDiff = append(prodDiff, []int{difficulty[i], profit[i]})
    }
    
    slices.SortFunc(prodDiff, func(x, y []int) int {
        return cmp.Compare(x[0], y[0])
    })
    
    clear(profit)
    var maxCurr = 0
    for i, p := range prodDiff {
        maxCurr = max(maxCurr, p[1])
        profit[i] = maxCurr
    }

    var ret = 0
    for _, w := range worker {
        var index = binSearch(w)
        if prodDiff[index][0] <= w {
            ret += profit[index]
        }
    }
    return ret
}