func heightChecker(heights []int) int {
    var sortedHeights = make([]int, len(heights))
    copy(sortedHeights, heights)
    slices.Sort(sortedHeights)
    var counts = 0
    
    for i := range len(heights) {
        if heights[i] != sortedHeights[i] {
            counts++
        }
    }
    return counts
}