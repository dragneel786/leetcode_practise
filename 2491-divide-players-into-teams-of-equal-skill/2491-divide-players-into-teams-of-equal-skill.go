func dividePlayers(skill []int) int64 {
    
    chemistry := 0
    slices.Sort(skill)
    start, end := 0, len(skill) - 1
    teamSum := skill[start] + skill[end]
    for start < end {
        if teamSum != skill[start] + skill[end]{
            return -1
        }
        chemistry += (skill[start] * skill[end])
        start += 1
        end -= 1
    }
    
    return int64(chemistry)
}