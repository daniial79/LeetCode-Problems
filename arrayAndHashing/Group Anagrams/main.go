package main

func main() {
}

func groupAnagrams(strs []string) [][]string {
	anagramBuckets := make(map[[26]int][]string)

	// Add each str to corresponding bucket
	// I used 'Valid Anagram' technique for generating key of each bucket
	for _, str := range strs {
		var count [26]int
		for _, char := range str {
			count[char-'a']++
		}
		anagramBuckets[count] = append(anagramBuckets[count], str)
	}

	// assign each bucket to result slice
	idx := 0
	result := make([][]string, len(anagramBuckets))
	for _, bucket := range anagramBuckets {
		result[idx] = bucket
		idx++
	}

	return result
}
