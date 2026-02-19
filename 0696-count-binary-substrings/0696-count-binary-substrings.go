func countBinarySubstrings(s string) int {
    prev, streak, res := 0, 1, 0
    for i := range len(s) - 1 {
        if s[i] == s[i + 1] {
            streak++
        } else {
            prev = streak
            streak = 1
        }

        if streak <= prev{
            res++
        }
    }

    return res
}