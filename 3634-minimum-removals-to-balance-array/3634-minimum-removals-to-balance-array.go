func minRemoval(nums []int, k int) int {
    //i [2, 12]
    //j [4, 24]
    n := len(nums)
    slices.Sort(nums[:])
    incValues := make([]int, len(nums))
    for i, val := range nums {
        incValues[i] = val * k
    }

    i, j := n - 1, n - 1
    res := 100000000
    // fmt.Println(nums, incValues)
    for i >= 0 && j >= 0 {
        if incValues[j] >= nums[i]{
            res = min(res, j + (n - i - 1))
            j--
        } else {
            i--
        }
    }

    if res == 100000000 {
        res = 0
    }
    return res
}

func min(a, b int) int{
    if a < b {
        return a
    }
    return b
}