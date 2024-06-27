func findCenter(edges [][]int) int {
    var n = len(edges) + 1
    var edgeCount = make(map[int]int)
    for _, edge := range edges {
        edgeCount[edge[0]]++
        if edgeCount[edge[0]] == n - 1 { return edge[0] }
        
        edgeCount[edge[1]]++
        if edgeCount[edge[1]] == n - 1 { return edge[1] }
    }
    
    return -1
}