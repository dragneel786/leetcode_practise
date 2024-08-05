func kthDistinct(arr []string, k int) string {
    var distinct = make(map[string]int)
    for _, a := range arr {
        distinct[a]++
    }
    
    var dCount = 0
    for _, a := range arr {
        if distinct[a] == 1 {
            dCount++
        }
        
        if dCount == k {
            return a
        }
    }
    
    return ""
}