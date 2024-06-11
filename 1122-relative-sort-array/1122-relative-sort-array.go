func relativeSortArray(arr1 []int, arr2 []int) []int {
    var numMap = make(map[int]int)
    for _, a := range arr1 {
        numMap[a]++
    }
    clear(arr1)
    
    var start = 0
    for _, a := range arr2 {
        for range numMap[a] {
            arr1[start] = a
            numMap[a]--
            start++
        }
    }
    
    var temp = []int{}
    for k, v := range numMap{
        for range v {
            temp = append(temp, k)
        }
    }
    slices.Sort(temp)
    // fmt.Println(start, temp, arr1)
    var tIndex = 0
    for start < len(arr1) {
        arr1[start] = temp[tIndex]
        tIndex++
        start++
    }
    
    return arr1
}