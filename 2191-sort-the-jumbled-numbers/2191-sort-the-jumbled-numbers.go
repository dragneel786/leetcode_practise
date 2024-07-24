func sortJumbled(mapping []int, nums []int) []int {
    var mappedNums = make(map[int][]int)
    for i, num := range nums {
        var temp = num
        var value = 0
        var mul = 1
        if num == 0 {
            value = mapping[0]
        } else {
            for num > 0 {
                value = (mapping[(num % 10)] * mul) + value
                num /= 10
                mul *= 10
            }
        }
        // fmt.Println(temp, value)
        mappedNums[temp] = []int{value, i}
    }
    sort.Slice(nums, func (i, j int) bool {
        if mappedNums[nums[i]][0] == mappedNums[nums[j]][0] {
            return mappedNums[nums[i]][1] < mappedNums[nums[j]][1]
        }
        
        return mappedNums[nums[i]][0] < mappedNums[nums[j]][0]
    })
    
    return nums
}