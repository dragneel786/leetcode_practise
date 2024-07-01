func threeConsecutiveOdds(arr []int) bool {
    var count = 0
    for _, a := range arr {
        var mod = a % 2
        if mod == 1 {
            count++
        } else {
            count = 0
        }
        if count >= 3 { return true }
    }
    
    return false
}