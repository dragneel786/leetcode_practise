func validStrings(n int) []string {
    var genString func(s string) []string;
    genString = func(s string) []string {
        if len(s) == n {
            return []string{s}
        }
        
        var res = genString(s + "1")
        if len(s) == 0 || s[len(s) - 1] == '1' {
            res = append(res, genString(s + "0")...)
        }
        return res
    }
    
    return genString("")
}