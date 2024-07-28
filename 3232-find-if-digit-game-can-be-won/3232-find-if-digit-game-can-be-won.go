func canAliceWin(nums []int) bool {
    var single, double = 0, 0
    for _, num := range nums {
        if num < 10 { 
            single += num
        } else { 
            double += num 
        }
    }
    
    return (single < double) || (double < single)
}