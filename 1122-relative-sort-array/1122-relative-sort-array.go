func relativeSortArray(arr1 []int, arr2 []int) []int {
    var indexMap = make(map[int]int)
    for i, a := range arr2 {
        indexMap[a] = i
    }
    slices.SortFunc(arr1, func(a, b int) int{
        aIndex, okA := indexMap[a]
        bIndex, okB := indexMap[b]
        if okA && okB {
            return cmp.Compare(aIndex, bIndex)
        } else if okA {
            return -1
        } else if okB{
            return 1
        } else {
            return cmp.Compare(a, b)
        }
    })

    return arr1
}