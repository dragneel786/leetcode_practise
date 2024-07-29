func numTeams(rating []int) int {
    var minMaxMap = make(map[int][]int)
    var ans = 0
    
    minMaxMap[rating[0]] = []int{0, 0} // mins, maxs
    for i := 1; i < len(rating); i++ {
        var mins, maxs = 0, 0
        for j := i - 1; j > -1; j-- {
            if rating[j] < rating[i] {
                mins++
                ans += minMaxMap[rating[j]][0]
            } else {
                maxs++
                ans += minMaxMap[rating[j]][1]
            }
        }
        minMaxMap[rating[i]] = []int{mins, maxs}
    }
    return ans
}