func buildMatrix(k int, rowConditions [][]int, colConditions [][]int) [][]int {
    
    var rowOrder = topoSort(k, &rowConditions)
    var colOrder = topoSort(k, &colConditions)
    if len(rowOrder) == 0 || len(colOrder) == 0 {
        return [][]int{}
    }

    var coors = make(map[int][]int)
    for i := range k { 
        coors[i + 1] = []int{rowOrder[i + 1], colOrder[i + 1]} 
    }

    var resultMatrix = [][]int{}
    for range k { resultMatrix = append(resultMatrix, make([]int, k))}

    for key, indexes := range coors {
        if resultMatrix[indexes[0]][indexes[1]] != 0 {
            return [][]int{}
        }
        resultMatrix[indexes[0]][indexes[1]] = key
    }

    return resultMatrix
}

func topoSort(k int, values *[][]int) map[int]int {
    var rowDegree = make([]int, k + 1)
    var rowMap = make(map[int][]int)
    for _, row := range *values {
        rowDegree[row[1]]++
        if _, ok := rowMap[row[0]]; !ok {
            rowMap[row[0]] = []int{}
        }
        rowMap[row[0]] = append(rowMap[row[0]], row[1])
    }

    var rowOrder = []int{}
    for i, d := range rowDegree[1:] {
        if d == 0 { rowOrder = append(rowOrder, i + 1) }
    }
    if len(rowOrder) == 0 {return make(map[int]int)}
    
    var index = 0
    var ret = make(map[int]int)
    for len(rowOrder) > 0 {
        var e = rowOrder[0]
        rowOrder = rowOrder[1:]
        ret[e] = index
        index++
        
        for _, v := range rowMap[e]{
            rowDegree[v]--
            if rowDegree[v] == 0 {
                rowOrder = append(rowOrder, v)
            }
        }
    }
    if len(ret) == k {
        return ret
    }

    return make(map[int]int)
}