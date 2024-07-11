func reverseParentheses(s string) string {
    var stack = list.New()
    for _, c := range s {
        if byte(c) == ')'{
            var values = []byte{}
            for stack.Back().Value.(byte) != '(' {
                values = append(values, stack.Back().Value.(byte))
                stack.Remove(stack.Back())
            }
            stack.Remove(stack.Back())
            for _, value := range values {
                stack.PushBack(value)
            }
        } else {
            stack.PushBack(byte(c))
        }
    }
    
    var res = ""
    for stack.Len() > 0 {
        res += string(stack.Front().Value.(byte))
        stack.Remove(stack.Front())
    }
    return res
}