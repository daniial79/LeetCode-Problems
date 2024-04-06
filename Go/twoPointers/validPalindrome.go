package twoPointers

func isAlphaNumeric(r rune) bool {
	if (r >= 65 && r <= 90) ||
		(r >= 97 && r <= 122) ||
		(r >= 48 && r <= 57) {
		return true
	}

	return false
}

func isUpperCase(r rune) bool {
	return (r >= 65 && r <= 90)
}

func IsPalindrome(s string) bool {

	leftPointer, rightPointer := 0, len(s)-1

	for leftPointer <= rightPointer {
		leftChar, rightChar := rune(s[leftPointer]), rune(s[rightPointer])

		if !isAlphaNumeric(leftChar) {
			leftPointer++
			continue
		}

		if !isAlphaNumeric(rightChar) {
			rightPointer--
			continue
		}

		if isUpperCase(leftChar) {
			leftChar += 32
		}

		if isUpperCase(rightChar) {
			rightChar += 32
		}

		if leftChar != rightChar {
			return false
		}

		leftPointer++
		rightPointer--

	}

	return true
}
