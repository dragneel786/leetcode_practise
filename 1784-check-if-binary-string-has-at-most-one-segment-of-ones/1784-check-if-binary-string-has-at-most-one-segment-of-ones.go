func checkOnesSegment(s string) bool {
    isOnesSeq := true
    for i := 0; i < len(s); i++ {
        if s[i] == '1'{
            if !isOnesSeq { return false }
        } else {
            isOnesSeq = false
        }
    }

    return true
}