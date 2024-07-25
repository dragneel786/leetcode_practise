func isValidSerialization(preorder string) bool {
    
    var isValid func (terms *[]string) bool
    isValid = func (terms *[]string) bool {
        if len(*terms) <= 0 {
            return false
        }
        var ch = (*terms)[0]
        *terms = (*terms)[1:]
        if ch == "#"{
            return true
        }
        
        var left = isValid(terms)
        var right = isValid(terms)
        return left && right
    }

    var splitTerms = strings.Split(preorder, ",")
    return isValid(&splitTerms) && len(splitTerms) == 0
}