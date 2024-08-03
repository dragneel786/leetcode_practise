func canBeEqual(target []int, arr []int) bool {
    var aMap = make(map[int]int)
    for _, a := range arr {
        aMap[a]++
    }
    
    for _, t := range target {
        _, ok := aMap[t]
        if !ok || aMap[t] <= 0 {
            return false
        }
        aMap[t]--
    }
    
    return true
}