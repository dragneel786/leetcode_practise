func scoreOfString(s string) int {
    var score = 0
    for i := 1; i < len(s); i++ {
        var diff = s[i - 1] - s[i]
        if s[i - 1] < s[i] {
            diff = s[i] - s[i - 1]
        }
        score += int(math.Abs(float64(diff)))
    }
    return score
}