func vowelConsonantScore(s string) int {
    vCounts, cCounts := 0, 0
    for _, c := range s {
        if !unicode.IsLetter(c) {
            continue
        }
        
        switch c {
            case 'a': vCounts++
            case 'e': vCounts++
            case 'i': vCounts++
            case 'o': vCounts++
            case 'u': vCounts++
            default: cCounts++
        } 
    }
    if cCounts > 0 {
        return div(vCounts, cCounts)
    }
    return 0
}

func div(a, b int) int {
    modu := a / b
    return int(math.Floor(float64(modu)))
}