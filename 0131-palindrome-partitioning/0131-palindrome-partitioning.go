func partition(s string) [][]string {
    var res = [][]string{}
    var dp = [][]bool{}
    var size = len(s)
    var palinParts func(index int, currStack []string)

    for range size {
        var temp = []bool{}
        for range size {
            temp = append(temp, false)
        }
        dp = append(dp, temp)
    }
    
    palinParts = func(index int, currStack []string) {
        if index >= len(s) {
            var temp = make([]string, len(currStack))
            copy(temp, currStack)
            res = append(res, temp)
            return
        }
        var str = ""
        for i := index; i < len(s); i++ {
            str += string(s[i])
            if str[0] == s[i] && (i - index <= 2 || dp[index + 1][i - 1]) {
                dp[index][i] = true
                palinParts(i + 1, append(currStack, str))
            }
        }
    }
    
    palinParts(0, []string{})
    return res
}