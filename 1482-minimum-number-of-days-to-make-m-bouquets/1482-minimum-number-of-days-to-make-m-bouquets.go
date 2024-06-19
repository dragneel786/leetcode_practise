func minDays(bloomDay []int, m int, k int) int {
    var n = len(bloomDay)
    if(n < m * k) { return -1 }
    
    var getKCounts = func (days int) int {
        var consCount, kCons = 0, 0
        for _, b := range bloomDay {
            if consCount == k {
                kCons++
                consCount = 0
            }
            if b > days{
                consCount = 0
            } else {
                consCount++
            }
        }
        
        return kCons
    }
    
    
    var low, high = 1, 0
    for _, b := range bloomDay {
        high = max(high, b)
    }
    
    var res = -1
    bloomDay = append(bloomDay, high + 1)
    for low <= high {
        var mid = (low + high) >> 1
        var kc = getKCounts(mid)
        if kc >= m {
            res = mid
            high = mid - 1
        } else {
            low = mid + 1
        }
    }
    
    return res
}