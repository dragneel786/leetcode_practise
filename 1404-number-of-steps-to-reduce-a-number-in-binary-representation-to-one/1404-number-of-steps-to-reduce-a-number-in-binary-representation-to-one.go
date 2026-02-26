func numSteps(s string) int {
    n := len(s)
    if n == 1 {
        return 0
    }
    if n == 2 {
        return 1
    }
    res, ones := 0, 0
    for i := n-1; i >= 0; i-- {
        if s[i] == '0' {
            res = res + 1 + ones
            if ones > 0 {
                ones = 1
            }
        } else {
            ones++
        }
    }
    if ones > 1 {
        res += ones + 1
    }
    
    return res
}