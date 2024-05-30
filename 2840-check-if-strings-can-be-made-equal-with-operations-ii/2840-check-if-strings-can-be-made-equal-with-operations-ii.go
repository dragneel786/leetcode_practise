func checkStrings(s1 string, s2 string) bool {
    var oddPlaces = make(map[rune]int)
    var evenPlaces = make(map[rune]int)
    for i, c := range s1 {
        if i % 2 == 1 {
            oddPlaces[c]++
        } else {
            evenPlaces[c]++
        }
    }
    
    
    for i, c := range s2 {
        if i % 2 == 1 {
            if oddPlaces[c] < 1 {
                return false
            }
            oddPlaces[c]--
            
            if oddPlaces[c] == 0 {
                delete(oddPlaces, c)
            }
            
        } else {
            if evenPlaces[c] < 1 {
                return false
            }
            evenPlaces[c]--
            
            if evenPlaces[c] == 0 {
                delete(evenPlaces, c)
            }
        }
    }
    
    return len(oddPlaces) == 0 && len(evenPlaces) == 0
}