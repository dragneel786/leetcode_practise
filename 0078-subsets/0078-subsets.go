func subsets(nums []int) [][]int {
    var res = [][]int{}
    var makeSubsets func(idx int, curr []int)
    
    makeSubsets = func (idx int, curr []int) {
        if idx >= len(nums){
            temp := make([]int, len(curr))
            copy(temp, curr)
            res = append(res, temp)
            return
        }
        makeSubsets(idx + 1, curr)
        makeSubsets(idx + 1, append(curr, nums[idx]))
    }
    
    makeSubsets(0, []int{})
    return res
}