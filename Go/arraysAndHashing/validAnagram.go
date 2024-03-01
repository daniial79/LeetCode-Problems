package arraysAndHashing

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
