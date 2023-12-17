package main

func main() {

}

func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	// Idea is keep track of alphabet frequency using a 26 sloth array
	var alphabetFrequencyTracker [26]int
	for i := 0; i < len(s); i++ {
		alphabetFrequencyTracker[s[i]-'a']++
		alphabetFrequencyTracker[t[i]-'a']--
	}

	// Check for non-zero element in array
	for i := 0; i < len(alphabetFrequencyTracker); i++ {
		if alphabetFrequencyTracker[i] != 0 {
			return false
		}
	}

	return true
}

func isAnagramD(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	letterFrequencyMap := make(map[int32]int)

	// Initiating letter frequency map
	for _, char := range s {
		if _, isThere := letterFrequencyMap[char]; isThere {
			letterFrequencyMap[char]++
			continue
		}
		letterFrequencyMap[char] = 1
	}

	// Remove instances from letter frequency map
	for _, char := range t {
		if _, isThere := letterFrequencyMap[char]; !isThere {
			return false
		}

		frequency := letterFrequencyMap[char]
		if frequency > 1 {
			letterFrequencyMap[char]--
		} else {
			delete(letterFrequencyMap, char)
		}
	}

	return len(letterFrequencyMap) == 0

}
