func separateDigits(nums []int) []int {
    res := []int{}
    for _, num := range nums {
        temp := []int{}
        for num > 0 {
            temp = append(temp, num % 10)
            num /= 10
        }
        for len(temp) > 0 {
            res = append(res, temp[len(temp)-1])
            temp = temp[:len(temp)-1]
        }
    }
    return res
}