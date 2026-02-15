func addBinary(a string, b string) string {
	i, j := len(a)-1, len(b)-1
	carry := 0

	var result strings.Builder

	for i >= 0 || j >= 0 || carry > 0 {
		sum := carry

		if i >= 0 {
			sum += int(a[i] - '0')
			i--
		}

		if j >= 0 {
			sum += int(b[j] - '0')
			j--
		}

		result.WriteByte(byte(sum%2) + '0')
		carry = sum / 2
	}

	// reverse the string since we built it backwards
	runes := []rune(result.String())
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}

	return string(runes)
}
