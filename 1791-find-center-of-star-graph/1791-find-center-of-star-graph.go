func findCenter(edges [][]int) int {
    var a, b = edges[0][0], edges[0][1]
    if edges[1][0] == a || edges[1][1] == a {
        return a
    }
    
    if edges[1][0] == b || edges[1][1] == b {
        return b
    }
    
    return -1
}