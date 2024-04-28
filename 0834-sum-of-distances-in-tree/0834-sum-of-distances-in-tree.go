func initTree(n int, edges [][]int) [][]int{
    tree := [][]int{}
    for range n {
        tree = append(tree, []int{})
    }

    for _, edge := range edges {
        tree[edge[0]] = append(tree[edge[0]], edge[1])
        tree[edge[1]] = append(tree[edge[1]], edge[0])
    }
    return tree
}

func sumOfDistancesInTree(n int, edges [][]int) []int {
    tree := initTree(n, edges)
    distance := make([]int, n)
    nodeCount := make([]int, n)

    dfsFirst(0, -1, 0, &tree, &distance, &nodeCount)
    dfsResult(0, -1, &tree, &distance, &nodeCount)
    return distance
}

func dfsFirst(node, parent, dist int, tree *[][]int,
     distance, nodeCount *[]int) int {
    for _, nei := range (*tree)[node] {
        if nei != parent {
            (*nodeCount)[node] += dfsFirst(nei, node, dist + 1, 
                tree, distance, nodeCount)
        }
    }
    (*nodeCount)[node]++
    (*distance)[0] += dist
    return (*nodeCount)[node]
}

func dfsResult(node, parent int, tree *[][]int, distance, nodeCount *[]int) {

    for _, nei := range (*tree)[node] {
        if nei != parent {
            (*distance)[nei] = (*distance)[node] - (*nodeCount)[nei] + (len(*tree) - (*nodeCount)[nei])
            dfsResult(nei, node, tree, distance, nodeCount)
        }
    }
}