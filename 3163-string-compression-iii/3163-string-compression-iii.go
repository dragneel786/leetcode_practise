func compressedString(word string) string {
    var currCount = 1
    var res = []string{}
    for i := range len(word) - 1 {
        if word[i] != word[i + 1] || currCount == 9 {
            res = append(res, strconv.Itoa(currCount))
            res = append(res, string(word[i]))
            currCount = 1
        } else {
            currCount++
        }
    }
    res = append(res, strconv.Itoa(currCount))
    res = append(res, string(word[len(word) - 1]))
    return strings.Join(res, "")
}