func furthestDistanceFromOrigin(moves string) int {
    lcount, rcount := 0, 0
    ucount := 0
    for _, c := range moves {
        switch ch := c; ch {
            case 'L': lcount++
            case 'R': rcount++
            default: ucount++
        }
    }
    return abs(lcount - rcount) + ucount
}

func abs(a int) int {
    if a < 0 {
        return -1 * a
    }
    return a
}