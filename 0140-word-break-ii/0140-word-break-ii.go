func wordBreak(s string, wordDict []string) []string {
    var wordDictMap = make(map[string]bool)
    for _, word := range wordDict {
        wordDictMap[word] = true
    }
    
    return wordBreakArrays(0, 0, s, []byte{}, &wordDictMap)
}

func wordBreakArrays(index, spaceIndex int, s string, currRun []byte,
                     wordDictMap *map[string]bool) []string {
    
    var word = string(currRun[spaceIndex:])
    if index >= len(s) {
        
        if (*wordDictMap)[word] {
            return []string{string(currRun)}
        }
        
        return []string{}
    }
    
    var ret = wordBreakArrays(index + 1, spaceIndex, s, append(currRun, s[index]), wordDictMap)
    if (*wordDictMap)[word] {
        ret = append(ret, wordBreakArrays(index, len(currRun) + 1, s,
                                          append(currRun, ' '), wordDictMap)...)
    }
    
    return ret
}