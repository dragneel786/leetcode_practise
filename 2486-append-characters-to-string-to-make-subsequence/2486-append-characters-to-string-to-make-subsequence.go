func appendCharacters(s string, t string) int {
    var sidx = 0
    for i, c := range t {
        for sidx < len(s) && rune(s[sidx]) != c {
            sidx++
        }
        
        if sidx >= len(s) {
            return len(t) - i
        }
        sidx++
    }
    
    return 0
}