func trimTrailingVowels(s string) string {
    n := len(s)
    i := n - 1
    for ; i > -1; i-- {
        switch ch := s[i]; ch {
            case 'a', 'e', 'i', 'o', 'u':
                continue
            default:
                return s[:i+1]
        } 
    }

    return ""
}