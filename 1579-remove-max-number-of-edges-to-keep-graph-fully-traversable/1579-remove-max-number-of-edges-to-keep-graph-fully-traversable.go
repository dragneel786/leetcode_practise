type DisjointSet struct {
    parents map[int]int
}

func NewDisjointSet(n int) *DisjointSet {
	ds := &DisjointSet{
		parents: make(map[int]int),
	}
	for i := range n {
		ds.parents[i + 1] = i + 1
	}
	return ds
}

func (this *DisjointSet) Find(p int) int {
    var px = this.parents[p]
    if px != p {
        this.parents[p] = this.Find(px)
    }
    return this.parents[p]
}

func (this *DisjointSet) Union(a, b int) bool {
    var pa, pb = this.Find(a), this.Find(b)
    if pa != pb {
        this.parents[pb] = pa
    }
    return pa == pb
}

func maxNumEdgesToRemove(n int, edges [][]int) int {
    var aliceGraph = NewDisjointSet(n)
    var bobGraph = NewDisjointSet(n)
    var deleted = 0
    
    slices.SortFunc(edges, func(a, b []int) int{
        return cmp.Compare(b[0], a[0])
    })
    // Type 3 handler
    for _, edge := range edges {
        if edge[0] == 3 {
            var a, b = aliceGraph.Union(edge[1], edge[2]), bobGraph.Union(edge[1], edge[2])
            if a == true && b == true {
                deleted++
            }
        } else if (edge[0] == 1 && aliceGraph.Union(edge[1], edge[2])) {
            deleted++
        } else if (edge[0] == 2 && bobGraph.Union(edge[1], edge[2])) {
            deleted++
        }
    }

    var parentA, parentB = aliceGraph.Find(1), bobGraph.Find(1)
    for i := 2; i <= n; i++ {
        if parentA != aliceGraph.Find(i) || parentB != bobGraph.Find(i) {
            return -1
        }
    }
    
    return deleted
}