func findDifferentBinaryString(nums []string) string {
    ans := []rune{}
    for i := 0; i < len(nums); i++ {
        curr := nums[i][i]
        add := '1' 
        if curr != '0' {
            add = '0'
        }
        ans = append(ans, add)
    }
    return string(ans)
}