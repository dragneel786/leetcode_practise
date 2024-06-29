func getAncestors(n int, edges [][]int) [][]int {
    var graph = make([][]int, n)
    for _, edge := range edges {
        graph[edge[0]] = append(graph[edge[0]], edge[1])
    }
    
    var res = make([][]int, n)
    for i := range n {
        populateAncestors(i, i, graph, res)
    }

    return res
}

func populateAncestors(a, c int, graph, res [][]int) {
    for _, cn := range graph[c] {
        if len(res[cn]) == 0 || res[cn][len(res[cn]) - 1] != a {
            res[cn] = append(res[cn], a)
            populateAncestors(a, cn, graph, res)
        }
    }
}