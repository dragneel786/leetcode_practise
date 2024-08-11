func finalPositionOfSnake(n int, commands []string) int {
    var cMap = make(map[string][]int)
    cMap["UP"] = []int{-1,0}
    cMap["DOWN"] = []int{1,0}
    cMap["LEFT"] = []int{0,-1}
    cMap["RIGHT"] = []int{0,1}
    
    var sr, sc = 0, 0
    for _, cmd := range commands {
        sr, sc = sr + cMap[cmd][0], sc + cMap[cmd][1]
    }
    return (n * sr) + sc
}