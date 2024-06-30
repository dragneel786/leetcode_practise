func minimumOperations(nums []int) int {
    var res = 0
    for _, num := range nums {
        var mod = (num % 3)
        res += min(mod, 3 - mod)
    }
    return res
}