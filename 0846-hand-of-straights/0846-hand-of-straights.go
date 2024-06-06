func isNStraightHand(hand []int, groupSize int) bool {
    slices.Sort(hand)
    var handCount = make(map[int]int)
    for _, v := range hand {
        handCount[v]++
    }
    
    var index = 0
    for index < len(hand) {
        for index < len(hand) && handCount[hand[index]] == 0 {
            index++
        }

        for inc := 0; index < len(hand) && inc < groupSize; inc++ {
            if handCount[hand[index] + inc] == 0 {
                return false
            }
            
            handCount[hand[index] + inc]--
        }
    }
    
    return true
}