func clearDigits(s string) string {
    var que = list.New()
    for _, c := range s {
        if unicode.IsDigit(c) {
            var e = que.Back()
			que.Remove(e)
        } else {
			que.PushBack(c)
		}
    }

	var ret = []string{}
	for que.Len() > 0 {
		var e = que.Front()
		ret = append(ret, string(e.Value.(rune)))
		que.Remove(e)
	} 
	
	return strings.Join(ret, "")
}