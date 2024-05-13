func minimumOperationsToMakeKPeriodic(word string, k int) int {
    mostOccurence := make(map[string]int)
    for i := 0; i + k <= len(word); i += k {
        subWord := word[i: i + k]
        if _, ok := mostOccurence[subWord]; !ok {
            mostOccurence[subWord] = 0
        }
        mostOccurence[subWord] += 1
    }
    
    maxVal := 0
    for _, value := range mostOccurence {
        maxVal = max(maxVal, value)
    }
    
    return len(word) / k - maxVal
}