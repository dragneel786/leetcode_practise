func countCompleteDayPairs(hours []int) int {
    var counts = 0
    for i, _ := range hours {
        for j, _ := range hours[i + 1:] {
            // fmt.Println(hours[i], hours[i + j + 1])
            if (hours[i] + hours[i + j + 1]) % 24 == 0 {
                counts++
            }
        }
    }
    return counts
}