func findLonely(nums []int) []int {
    var numsCount = make(map[int]int)
    for _, num := range nums {
        if _, ok := numsCount[num]; !ok {
            numsCount[num] = 0
        }
        numsCount[num]++
    }
    
    var res = []int{}
    for _, num := range nums {
        if numsCount[num] > 1 || numsCount[num-1] != 0 || numsCount[num+1] != 0 {
            continue
        }
        
        res = append(res, num)
    }
    
    return res
}