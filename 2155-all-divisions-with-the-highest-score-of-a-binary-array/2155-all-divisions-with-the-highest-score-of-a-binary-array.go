func maxScoreIndices(nums []int) []int {
    var ones = 0
    nums = append(nums, -1)
    for _, num := range nums {
        if num == 1 {
            ones++
        }
    }
    
    var res = []int{}
    var zeros, count = 0, 0
    for i, num := range nums {
        var sums = zeros + ones
        if sums >= count {
            if sums > count{
                res = []int{}
            }
            count = sums
            res = append(res, i)
        }
        
        if num == 0 {
            zeros++
        } else {
            ones--
        }
        
    }
    
    return res
}