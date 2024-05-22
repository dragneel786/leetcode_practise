func partition(s string) [][]string {
    var res = [][]string{}
    var palinParts func(index int, isPalin bool, currStack []string)
    
    isPalindrome := func(str string) bool {
        var size = len(str)
        for i := range size / 2 {
            if str[i] != str[size - i - 1] {
                return false
            }
        }
        return true
    }
    
    palinParts = func(index int, isPalin bool, currStack []string) {
        if index >= len(s) {
            if isPalin {
                var temp = make([]string, len(currStack))
                copy(temp, currStack)
                res = append(res, temp)
            }
            return
        }
        
        for i := index; i < len(s); i++ {
            palinParts(i + 1, isPalin && isPalindrome(string(s[index: i + 1])), append(currStack, s[index: i + 1]))
        }
    }
    palinParts(0, true, []string{})
    return res
}