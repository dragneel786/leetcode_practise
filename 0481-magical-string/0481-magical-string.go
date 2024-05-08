func magicalString(n int) int {
    arr := []int{2}
    ones := 1
    n -= 3
    for n > 0 {
        val := 2
        if arr[len(arr) - 1] != 1 { 
            val = 1 
            ones++
        }
        arr = append(arr, val)
        n--
        
        if n > 0 && arr[0] == 2 {
            arr = append(arr, val)
            if val == 1 {
                ones++
            }
            n--
        }
        arr = arr[1:]
    }
    // fmt.Println(arr)
    return ones
}