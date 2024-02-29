package main

func containsDuplicate(nums []int) bool {
	// Check for empty array
	if len(nums) < 1 {
		return true
	}

	// Keep track of existence of elements that are visited before
	exists := make(map[int]int)

	for _, n := range nums {
		// Check if element is already in existence array
		if _, ok := exists[n]; ok {
			return true
		} else {
			exists[n] = 1
		}
	}

	// No duplicated elements
	return false
}
