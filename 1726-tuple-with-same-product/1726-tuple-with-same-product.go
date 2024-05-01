func tupleSameProduct(nums []int) int {
    size := len(nums)
    productCounts := make(map[int]int)
    for i := range size {
        for j := i + 1; j < size; j++ {
            prod := nums[i] * nums[j]
            if _, ok := productCounts[prod]; !ok {
                productCounts[prod] = 0
            }
            productCounts[prod]++
        }
    }
    
    ans := 0
    for _, value := range productCounts {
        if(value >= 2) {
            ans += int(fact(value) / (fact(2) * fact(value - 2))) * 8
        }
    }
    return ans
}

func fact(n int) int {
    res := 1
    for i := 1; i < n + 1; i++ { res *= i }
    return res
}