type DisjointSet struct {
    Parent map[int]int
}

func (ds *DisjointSet) Find(x int) int{
    if(ds.Parent[x] != x) {
        ds.Parent[x] = ds.Find(ds.Parent[x])
    }
    return ds.Parent[x]
}

func (ds *DisjointSet) Union(x, y int) {
    px, py := ds.Find(ds.Parent[x]), ds.Find(ds.Parent[y])
    if px != py {
        ds.Parent[py] = px
    }
}

func NewDisjointSet(elements []int) *DisjointSet {
    ret := &DisjointSet{Parent: make(map[int]int)}
    for _, e := range elements {
        ret.Parent[e] = e
    }
    return ret   
}

func validPath(n int, edges [][]int, source int, destination int) bool {
    elements := make([]int, n)
    for i := 0; i < n; i++ {
        elements[i] = i
    }
    ds := NewDisjointSet(elements)
    for _, edge := range edges {
        ds.Union(edge[0], edge[1])
    }
    return ds.Find(source) == ds.Find(destination)
}