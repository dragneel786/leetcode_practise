func Constructor(edges [][]int) map[int]map[int]bool {
    tree := make(map[int]map[int]bool)
    for _, edge := range edges {
        if _, ok := tree[edge[0]]; !ok {
            tree[edge[0]] = make(map[int]bool)
        }
        tree[edge[0]][edge[1]] = true

        if _, ok := tree[edge[1]]; !ok {
            tree[edge[1]] = make(map[int]bool)
        }
        tree[edge[1]][edge[0]] = true
    }
    return tree
}

func findMinHeightTrees(n int, edges [][]int) []int {
    if n < 3{
        ret := make([]int, n)
        for i := range n{
            ret[i] = i
        }
        return ret
    }
    tree := Constructor(edges)
    que := make(chan int, n)
    for key, value := range tree {
        if len(value) == 1 {
            que <- key
        }
    }
    remainNodes := n
    for remainNodes > 2 {
        remainNodes -= len(que)
        for range len(que) {
            leaf := <- que
            for key, _ := range tree[leaf] {
                delete(tree[key], leaf)
                if len(tree[key]) == 1{
                    que <- key
                }

                delete(tree[leaf], key)
            }
        }
    }
    
    ret := make([]int, 0)
    for range len(que) {
        ret = append(ret, <- que)
    }
    return ret
}