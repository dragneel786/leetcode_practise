func residuePrefixes(s string) int {
    ans := 0
    uniqueChars := make(map[rune]bool)
    for i, c := range s {
        if _, ok := uniqueChars[c]; !ok {
            uniqueChars[c] = true
        }
        if len(uniqueChars) == ((i + 1) % 3){
            ans++
        }
    }
    return ans
}