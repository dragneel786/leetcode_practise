func frequencySort(nums []int) []int {
    var counts = make(map[int]int)
    for _, num := range nums {
        counts[num]++
    }
    var values = [][]int{}
    for k, v := range counts {
        values = append(values, []int{v, k})
    }
    
    sort.Slice(values, func (i, j int) bool {
        if values[i][0] == values[j][0] {
            return values[i][1] > values[j][1]
        }
        
        return values[i][0] < values[j][0]
    })
     
    var index = 0
    for _, val := range values {
        for range val[0] {
            nums[index] = val[1]
            index++
        }
    }
    
    return nums
}