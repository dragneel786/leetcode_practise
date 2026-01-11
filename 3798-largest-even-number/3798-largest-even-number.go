func largestEven(s string) string {
    chars := []rune(s)
    for ;len(chars) > 0; {
        if int(chars[len(chars) - 1]) % 2 == 0 { break }
        chars = chars[:len(chars) - 1]
    }
    
    return string(chars)
}