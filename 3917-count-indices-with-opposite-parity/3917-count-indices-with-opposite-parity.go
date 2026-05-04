func countOppositeParity(nums []int) []int {
    n := len(nums)
    odds, evens := 0, 0
    for i := range n {
        if nums[i] % 2 == 0 {
            evens++
        } else {
            odds++
        } 
    }

    res := make([]int, n)
    for i := range n {
        if nums[i] % 2 == 0 {
            evens--
            res[i] = odds
        } else {
            odds--
            res[i] = evens
        }
    }
    return res
}