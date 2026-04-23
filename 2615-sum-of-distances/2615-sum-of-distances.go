func distance(nums []int) []int64 {
    indexListMap := make(map[int][]int)
    for i, num := range nums {
        if _, ok := indexListMap[num]; !ok {
            indexListMap[num] = []int{}
        }

        indexListMap[num] = append(indexListMap[num], i)
    }

    arr := make([]int64, len(nums))
    for _, group := range indexListMap {
        tot := 0
        for _, g := range group {
            tot += g
        }
        
        size := len(group)
        prefixTot := 0
        for i, idx := range group {
            val := tot - prefixTot * 2 + idx * (2 * i - size)
            arr[idx] = int64(val)
            prefixTot += idx
        }
    }
    
    return arr
}

func abs(val int) int {
    if val < 0 {
        return -1 * val
    }
    return val
}