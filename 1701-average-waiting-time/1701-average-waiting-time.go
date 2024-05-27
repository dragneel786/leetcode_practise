func averageWaitingTime(customers [][]int) float64 {
    var curr = -1
    var total = 0
    for _, cust := range customers {
        if cust[0] > curr {
            curr = cust[0]
        }
        
        curr += cust[1]
        total += curr - cust[0]
    }
    
    return float64(total) / float64(len(customers))
}