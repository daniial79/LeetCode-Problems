package main

func productExceptSelf(nums []int) []int {
	answer := make([]int, len(nums))
	prefixProductArr := make([]int, len(nums))
	suffixProductArr := make([]int, len(nums))

	// Initiate the prefix product array
	prefixProductArr[0] = 1
	for i := 1; i < len(nums); i++ {
		prefixProductArr[i] = nums[i-1] * prefixProductArr[i-1]
	}

	// Initiate the suffix product array
	suffixProductArr[len(nums)-1] = 1
	for i := len(nums) - 2; i >= 0; i-- {
		suffixProductArr[i] = nums[i+1] * suffixProductArr[i+1]
	}

	for i := 0; i < len(nums); i++ {
		answer[i] = prefixProductArr[i] * suffixProductArr[i]
	}

	return answer
}
