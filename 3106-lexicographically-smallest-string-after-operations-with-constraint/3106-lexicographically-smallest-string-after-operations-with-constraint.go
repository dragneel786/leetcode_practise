func getSmallestString(s string, k int) string {
    var res = []string{}
    for _, c := range s {
        for i := range 26 {
            var intVal = int(c)
            var diff = intVal - (97 + i)
            var minDiff = min(diff, 26 - diff)
            if minDiff <= k {
                k -= minDiff
                res = append(res, string(byte(97 + i)))
                break
            }
        }
    }
    return strings.Join(res, "")
}