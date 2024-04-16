package twoPointers

func TwoSum(numbers []int, target int) []int {
	left, right := 0, len(numbers)-1

	for left < right {
		candidate := numbers[left] + numbers[right]

		if candidate > target {
			// Decrease the candidate value
			if numbers[right-1] != numbers[right] {
				right--
			} else {
				for numbers[right-1] == numbers[right] {
					right--
				}
			}
		} else if candidate < target {
			// Increase the candidate
			if numbers[left+1] != numbers[left] {
				left++
			} else {
				for numbers[left+1] == numbers[left] {
					left++
				}
			}
		} else {
			return []int{left + 1, right + 1}
		}

	}

	return []int{}

}
