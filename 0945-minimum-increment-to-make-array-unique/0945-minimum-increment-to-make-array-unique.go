func minIncrementForUnique(nums []int) int {
    var numMap = make(map[int]int)
    for _, num := range nums {
        numMap[num]++
    }

    var moves = 0
    var maxVal = int(math.Pow10(5)) + 1
    for i := 0; i <= maxVal || numMap[i] > 1; i++ {
        if numMap[i] > 1{
            moves += numMap[i] - 1
            numMap[i + 1] += numMap[i] - 1
        }
    }
    return moves
}