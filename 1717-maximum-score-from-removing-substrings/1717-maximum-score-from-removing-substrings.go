func maximumGain(s string, x int, y int) int {
    var score = 0
    if x > y { 
        removePoints(removePoints(s, "ab", x, &score), "ba", y, &score) 
    } else {
        removePoints(removePoints(s, "ba", y, &score), "ab", x, &score)
    }
    return score
}

func removePoints(s, remove string, points int, score *int) string {
    var ret = []byte{}
    for _, c := range s {
        if len(ret) > 0 && ret[len(ret) - 1] == remove[0] && byte(c) == remove[1] {
            ret = ret[:len(ret) - 1]
            *score += points
        } else {
            ret = append(ret, byte(c))
        }
    }
    
    return string(ret)
}