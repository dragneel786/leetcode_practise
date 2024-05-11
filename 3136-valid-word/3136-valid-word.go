func isValid(word string) bool {
    if len(word) < 3 { return false }
    
    hasVowels := false
    hasConsonant := false
    vowels := map[rune]bool{'a':true, 'e':true, 'i':true, 'o':true, 'u':true}
    for _, c := range word {
        if unicode.IsLetter(c) {
			if vowels[unicode.ToLower(c)] {
				hasVowels = true
			} else {
				hasConsonant = true
			}
        } else if !unicode.IsDigit(c) {
			return false
		}
    }
    return hasVowels && hasConsonant
}