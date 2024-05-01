func tupleSameProduct(nums []int) int {
    var fact func(n int) int;
    cache := make(map[int]int)
    cache[1] = 1
    cache[0] = 1
    
    fact = func(n int) int {
        if _, ok := cache[n]; ok{
            return cache[n]
        }
        cache[n] = n * fact(n - 1)
        return cache[n]
    }
    
    
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