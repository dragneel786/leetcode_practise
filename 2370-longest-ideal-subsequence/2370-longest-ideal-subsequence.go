func longestIdealString(s string, k int) int {
    size := len(s)
    charMap := make(map[rune]int)
    for _, c := range "abcdefghijklmnopqrstuvwxyz" {
        charMap[c] = 0
    }

    dp := make([]int, size)
    res := 0
    for i, char := range s {
        maxSoFar := 0
        for key, value := range charMap{
            if int(math.Abs(float64(key) - float64(char))) <= k{
                maxSoFar = max(maxSoFar, value)
            }
        }
        dp[i] = maxSoFar + 1
        charMap[char] = max(charMap[char], dp[i])
        res = max(dp[i], res)
    }

    return res
}