func maximumImportance(n int, roads [][]int) int64 {
    var nodeCount = make(map[int]int)
    for _, road := range roads {
        nodeCount[road[0]]++
        nodeCount[road[1]]++
    }
    
    var nodeWithCount = [][]int{}
    for key, value := range nodeCount {
        nodeWithCount = append(nodeWithCount, []int{value, key})
    }
    
    slices.SortFunc(nodeWithCount, func (a, b []int) int {
        return cmp.Compare(b[0], a[0])
    })
    
    var count = n
    for _, value := range nodeWithCount {
        nodeCount[value[1]] = count
        count--
    }
    
    var res = 0
    for _, road := range roads {
        res += nodeCount[road[0]] + nodeCount[road[1]]
    }
    return int64(res)
}