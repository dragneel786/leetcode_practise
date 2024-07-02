func intersect(nums1 []int, nums2 []int) []int {
    var counts = make(map[int]int)
    for _, num := range nums1 {
        counts[num]++
    }
    
    var res = []int{}
    for _, num := range nums2 {
        if counts[num] > 0 {
            res = append(res, num)
            counts[num]--
        }
    }
    return res
}