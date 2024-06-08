func lastNonEmptyString(s string) string {
    var occur = make(map[rune]int)
    var maxOccur = 0
    var ret = []string{}
    for _, c := range s {
        occur[c]++
        if maxOccur <= occur[c] {
            if maxOccur < occur[c] { ret = []string{} }
            ret = append(ret, string(c))
            maxOccur = occur[c]
        }

    }
    return strings.Join(ret, "")
}