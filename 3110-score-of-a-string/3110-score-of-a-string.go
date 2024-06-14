func scoreOfString(s string) int {
    var score = 0
    for i := 1; i < len(s); i++ {
        score += int(math.Abs(float64(int(s[i - 1]) - int(s[i]))))
    }
    return score
}