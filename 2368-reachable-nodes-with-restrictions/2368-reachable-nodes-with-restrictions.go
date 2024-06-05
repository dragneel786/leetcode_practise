func reachableNodes(n int, edges [][]int, restricted []int) int {
    var graph = make(map[int][]int)
    for _, edge := range edges {
        var a, b = edge[0], edge[1]
        if _, ok := graph[a]; !ok {
            graph[a] = []int{}
        }
        graph[a] = append(graph[a], b)
        
        if _, ok := graph[b]; !ok {
            graph[b] = []int{}
        }
        graph[b] = append(graph[b], a)
    }
    
    var restrictMap = make(map[int]bool)
    for _, r := range restricted {
        restrictMap[r] = true
    }
    
    return reachNodes(0, &restrictMap, &graph)
}

func reachNodes(node int, restrictMap *map[int]bool, graph *map[int][]int) int{
    var ret = 0
    (*restrictMap)[node] = true
    for _, nei := range (*graph)[node] {
        if !(*restrictMap)[nei] {
            ret += reachNodes(nei, restrictMap, graph)
        }
    }
    (*restrictMap)[node] = false
    return ret + 1
}