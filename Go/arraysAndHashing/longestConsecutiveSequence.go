package arraysAndHashing

func longestConsecutive(nums []int) int {
	max_length := 0
	numbers_set := make(map[int]bool)

	for _, number := range nums {
		if numbers_set[number] {
			continue
		}
		numbers_set[number] = true
	}

	for number := range numbers_set {
		if numbers_set[number-1] {
			continue
		}

		sequence := 1
		temp := number + 1

		for numbers_set[temp] {
			sequence++
			temp++
		}

		if sequence > max_length {
			max_length = sequence
		}
	}

	return max_length
}
