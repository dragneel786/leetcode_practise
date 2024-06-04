func minimumChairs(s string) int {
    var maxE, currE = 0, 0
    for _, c := range s {
        if string(c) == "E" {
            currE++
        } else {
            currE-- 
        }
        maxE = max(maxE, currE)
    }
    return maxE
}