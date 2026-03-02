func minSwaps(grid [][]int) int {
    n := len(grid)
    counts := []int{}
    for _, g := range grid {
        curr_count := 0
        for i := n - 1; i > -1; i-- {
            if g[i] == 1 {
                break
            }
            curr_count++
        }
        counts = append(counts, curr_count)
    }
    fmt.Println(counts)
    moves := 0
    need := n - 1
    for i := range n - 1 {
        j := i
        for ;j < n; j++ {
            if counts[j] >= need {
                break
            }
        }

        if j == n {
            return -1
        }
        fmt.Println(i, j)

        for ;j > i; j-- {
            counts[j], counts[j - 1] = counts[j - 1], counts[j]
            moves++
        }
        need--
        // fmt.Println(counts, need)
    }
    return moves
}