func countVowels(word string) int64 {
    var res = 0
    for i, w := range word {
        var ch = byte(w)
        if ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' {
            res += (i + 1) * (len(word) - i)
        }
    }
    return int64(res)
}