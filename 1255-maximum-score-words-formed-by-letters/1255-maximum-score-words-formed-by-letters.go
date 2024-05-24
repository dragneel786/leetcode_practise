func maxScoreWords(words []string, letters []byte, score []int) int {
    
    var getSubsetScore = func (subSetsWords []string, ) int {
        var lettersCount = make(map[byte]int)
        for _, l := range letters {
            lettersCount[l]++
        }
        
        var res = 0
        for _, word := range subSetsWords {
            var isFormable = true
            var currScore = 0

            for _, c := range word {
                currScore += score[c - 97]
                lettersCount[byte(c)]--
                if lettersCount[byte(c)] < 0 {
                    isFormable = false
                    break
                }
            }

            if isFormable {
                res += currScore
            }
        }
        return res
    }
    
    var subsets func(index int, curr []string) int
    subsets = func(index int, curr []string) int {
        if index >= len(words){
            return getSubsetScore(curr)
        }
        
        return max(subsets(index + 1, append(curr, words[index])), subsets(index + 1, curr))
    }
    
    return subsets(0, []string{})
}
