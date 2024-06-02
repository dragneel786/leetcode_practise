func maxUniqueSplit(s string) int {
    var uniq = make(map[string]bool)
    var splitsCounts func(start, end int) int;
    
    splitsCounts = func (start, end int) int {
        if end >= len(s) {
            return 0
        }
        
        var ret = splitsCounts(start, end + 1)
        if !uniq[s[start : end + 1]] {
            uniq[s[start : end + 1]] = true
            
            ret = max(ret, 1 + splitsCounts(end + 1, end + 1))
            uniq[s[start : end + 1]] = false
        }
        return ret
    }
    
    return splitsCounts(0, 0)
}