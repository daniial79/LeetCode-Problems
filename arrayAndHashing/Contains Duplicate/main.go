package main

import "fmt"

func main() {
	fmt.Println([]int{1, 2, 3, 4})
	fmt.Println([]int{1, 1, 2, 3})
}

func containsDuplicate(nums []int) bool {
	// Check for empty array
	if len(nums) < 1 {
		return true
	}

	// Keep track of existence of elements that are visited before
	exists := make(map[int]struct{})

	for _, n := range nums {
		// Check if element is already in existence array
		if _, ok := exists[n]; ok {
			return true
		} else {
			exists[n] = struct{}{}
		}
	}

	// No duplicated elements
	return false
}
