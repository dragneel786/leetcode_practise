func sortColors(nums []int)  {
    var c0, c1, c2 = 0, 0, 0
    for _, num := range nums {
        if num == 0 {
            c0++
        } else if num == 1 {
            c1++
        } else {
            c2++
        }
    }
    
    for i := range len(nums){
        if c0 > 0 {
            nums[i] = 0
            c0--
        } else if c1 > 0 {
            nums[i] = 1
            c1--
        } else {
            nums[i] = 2
        }
    }
}