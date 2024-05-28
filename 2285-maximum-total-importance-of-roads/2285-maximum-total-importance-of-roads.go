func maximumImportance(n int, roads [][]int) int64 {
    var graph = make([]int, n)
    for _, road := range roads {
        graph[road[0]]++
        graph[road[1]]++
    }
    slices.Sort(graph)
    
    var res = 0
    for i := range n {
        res += graph[i] * (i + 1)
    }
    
    return int64(res)
}