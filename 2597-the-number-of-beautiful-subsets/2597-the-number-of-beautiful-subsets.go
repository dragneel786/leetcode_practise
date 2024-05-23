func beautifulSubsets(nums []int, k int) int {
    var chooseMap = make([]int, 1001)
    slices.Sort(nums)
    
    var countSubsets func(index, count int) int;
    countSubsets = func(index, count int) int {
        if index >= len(nums) {
            if count > 0 {
                return 1
            }
            return 0
        }
        
        var ret = countSubsets(index + 1, count)
        if nums[index] - k <= 0 || chooseMap[nums[index] - k] == 0 {
            chooseMap[nums[index]]++
            ret += countSubsets(index + 1, count + 1)
            chooseMap[nums[index]]--
        }

        return ret
    }
    
    return countSubsets(0, 0)
}