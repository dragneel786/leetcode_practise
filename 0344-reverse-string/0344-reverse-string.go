func reverseString(s []byte)  {
    var size = len(s)
    for i := 0; i < (size / 2); i++ {
        s[i], s[size - i - 1] = s[size - i - 1], s[i]
    }
}