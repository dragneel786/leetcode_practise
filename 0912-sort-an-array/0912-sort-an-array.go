func sortArray(nums []int) []int {
    var upto = 1_00_001
    var arr = make([]int, upto)
    for _, num := range nums {
        arr[num + 50000]++
    }

    var index = 0
    for i, v := range arr {
        for range v {
            nums[index] = i - 50000
            index++
        }
    }
    return nums
}