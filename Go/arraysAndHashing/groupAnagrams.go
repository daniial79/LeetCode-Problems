package arraysAndHashing

func groupAnagrams(strs []string) [][]string {
	anagramBuckets := make(map[[26]int][]string)

	for _, str := range strs {
		var count [26]int
		for _, char := range str {
			count[char-'a']++
		}
		anagramBuckets[count] = append(anagramBuckets[count], str)
	}

	idx := 0
	result := make([][]string, len(anagramBuckets))
	for _, bucket := range anagramBuckets {
		result[idx] = bucket
		idx++
	}

	return result
}
