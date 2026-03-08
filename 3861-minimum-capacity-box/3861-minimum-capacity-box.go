func minimumIndex(capacity []int, itemSize int) int {
    index, diff := -1, 10000
    for i, cap := range capacity {
        currDiff := cap - itemSize
        if currDiff > -1 && currDiff < diff {
            diff = currDiff
            index = i
        }
    }
    return index
}