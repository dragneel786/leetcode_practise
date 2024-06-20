func maxDistance(position []int, m int) int {
    
    var isPossible = func(val int) bool {
        var prev = position[0]
        var ballsPlaced = 1
        for i := 1; i < len(position); i++ {
            if position[i] - prev >= val {
                prev = position[i]
                ballsPlaced += 1
            }
        }
        
        return ballsPlaced >= m
    }
    
    slices.Sort(position)
    var low, high = 0, 0
    for _, p := range position {
        high = max(high, p)
    }
    
    var res = 0
    for low <= high {
        var mid = (low + high) >> 1
        var possible = isPossible(mid)
        if possible {
            res = mid
            low = mid + 1
        } else {
            high = mid - 1
        }
    }
    
    return res
}