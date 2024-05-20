func subsetXORSum(nums []int) int {
    var res = 0
    var genSubsets func(index, val int)
    genSubsets = func(index, val int) {
        if index >= len(nums) { 
            res += val
            return 
        }
        genSubsets(index + 1, val)
        genSubsets(index + 1, val ^ nums[index])
    }
    
    genSubsets(0, 0)
    return res
}

