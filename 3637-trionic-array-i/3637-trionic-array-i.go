func isTrionic(nums []int) bool {
    n, i := len(nums), 1
    for i < n - 1 && nums[i - 1] < nums[i] {
        i++ 
    }
    p := i - 1

    for i < n - 1 && nums[i - 1] > nums[i] {
        i++
    }
    q := i - 1

    for i < n && nums[i - 1] < nums[i] {
        i++
    }
    flag := i - 1

    return (p != 0) && (p != q) && (flag == n - 1 && flag != q)

}