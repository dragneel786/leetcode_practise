func occurrencesOfElement(nums []int, queries []int, x int) []int {
    var occurIndex = []int{}
    for i, num := range nums {
        if num == x {
            occurIndex = append(occurIndex, i)
        }
    }
    
    
    var res = []int{}
    for _, q := range queries {
        if len(occurIndex) >= q {
            res = append(res, occurIndex[q - 1])
        } else {
            res = append(res, -1)
        }
    }
    
    return res
}