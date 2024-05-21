func twoEditWords(queries []string, dictionary []string) []string {
    var res = []string{}
    for _, word := range queries{
        for _, dict := range dictionary {
            
            var diffCount = 0
            for i := 0; i < len(word); i++ {
                if word[i] != dict[i] {
                    diffCount++
                }
                
                if diffCount > 2{
                    break
                }
            }
            
            if diffCount < 3{
                res = append(res, word)
                break
            }
        }
    }
    return res
}