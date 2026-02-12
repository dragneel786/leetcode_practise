func reverseByType(s string) string {
    specialChars := []rune{}
    chars := []rune{}
    for _, c := range s {
        if unicode.IsLower(c) {
            chars = append(chars, c)
        } else {
            specialChars = append(specialChars, c)
        }
    }
    
    res := []rune{}
    for _, c := range s {
        if unicode.IsLower(c) {
            res = append(res, chars[len(chars) - 1])
            chars = chars[:len(chars) - 1]
        } else {
            res = append(res, specialChars[len(specialChars) - 1])
            specialChars = specialChars[:len(specialChars) - 1]
        }
    }

    return string(res)
}