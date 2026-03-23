func mapWordWeights(words []string, weights []int) string {
    res := make([]rune, 0, len(words))

    for _, word := range words {
        tot := 0
        for _, c := range word {
            index := c - 'a'
            tot += weights[index]
        }
        res = append(res, 'z' - rune(tot % 26))
    }
    return string(res)
}