func numberOfSpecialChars(word string) int {
    upperCase := make(map[rune]int)
    lowerCase := make(map[rune]int)
    for i, c := range word {
        if _, ok := upperCase[c]; unicode.IsUpper(c) && !ok{
            upperCase[c] = i
        }

        if unicode.IsLower(c){
            runeChar := []rune(strings.ToUpper(string(c)))
            lowerCase[runeChar[0]] = i
        }
    }

    specials := 0
    for key, uIndex := range upperCase {
        if lIndex, ok := lowerCase[key]; ok && lIndex < uIndex {
            specials++
        }
    }
    return specials
}