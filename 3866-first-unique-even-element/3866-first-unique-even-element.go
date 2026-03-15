func firstUniqueEven(nums []int) int {
    numSet := make(map[int]int)
    for _, num := range nums {
        numSet[num]++
    }

    for _, num := range nums {
        if(num % 2 == 0 && numSet[num] == 1) {
            return num
        }
    }

    return -1
}