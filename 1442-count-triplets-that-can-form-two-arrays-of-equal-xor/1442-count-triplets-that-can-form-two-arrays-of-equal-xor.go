func countTriplets(arr []int) int {
    var xorArr = []int{}
    xorArr = append(xorArr, arr[0])
    for _, a := range arr[1:] {
        xorArr = append(xorArr, xorArr[len(xorArr) - 1] ^ a)
    }
    
    var counts = 0
    for i := range len(arr) {
        var subPrev = 0
        if i > 0 {
            subPrev = xorArr[i - 1]
        }
        
        for j := i + 1; j < len(arr); j++ {
            if subPrev ^ xorArr[j] == 0 {
                counts += (j - i)
            }
        }
    }
    
    return counts
}