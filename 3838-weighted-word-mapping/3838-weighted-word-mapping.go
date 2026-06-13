func mapWordWeights(words []string, weights []int) string {
	var values []rune

	for _, word := range words {
		tot := 0

		for _, c := range word {
			idx := int(c - 'a')
			tot += weights[idx]
		}

		mod := tot % 26
		values = append(values, rune('a'+ (25 - mod)))
	}

	return string(values)
}