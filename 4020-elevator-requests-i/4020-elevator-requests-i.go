func elevatorRequests(n int, requests []int) int {
    tot := 0
    prev := 0
    for _, r := range requests {
        tot += abs(prev - r)
        prev = r
    }
    return tot
}

func abs(val int) int {
    if(val < 0) {
        return val * -1
    }
    return val
}