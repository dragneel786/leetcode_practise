func numberOfAlternatingGroups(colors []int) int {
    var size = len(colors)
    var counts = 0
    for i := range size {
        var nIndex = (i + 1) % size
        var nnIndex = (i + 2) % size
        if colors[i] != colors[nIndex] && colors[nIndex] != colors[nnIndex] {
            counts++
        }
    }
    return counts
}