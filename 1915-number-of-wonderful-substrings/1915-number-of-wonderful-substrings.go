func wonderfulSubstrings(word string) int64 {
    bitMask := 0
    bitMap := make(map[int]int)
    bitMap[0] = 1
    res := 0
    
    for _, w := range word {
        index := int(w) - 97
        bitMask ^=  (1 << index)
        
        if _, ok := bitMap[bitMask]; !ok {
            bitMap[bitMask] = 0
        }
        res += bitMap[bitMask]
        bitMap[bitMask]++
        res += check(&bitMap, bitMask)
    }
    return int64(res)
}

func check(bitMap *map[int]int, bitMask int) int {
    counts := 0
    for i := range 10 {
        oneBitDiff := bitMask ^ (1 << i)
        if _, ok := (*bitMap)[oneBitDiff]; ok {
            counts += (*bitMap)[oneBitDiff]
        }
    }
    return counts
}