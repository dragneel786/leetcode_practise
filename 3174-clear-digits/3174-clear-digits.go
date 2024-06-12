func clearDigits(s string) string {
    var que = []string{}
    for _, c := range s {
        if unicode.IsDigit(c) {
            que = que[:len(que) - 1]
        } else {
            que = append(que, string(c))
		}
    }
	
	return strings.Join(que, "")
}