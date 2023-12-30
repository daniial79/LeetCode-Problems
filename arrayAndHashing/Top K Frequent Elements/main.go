package main

func topKFrequent(nums []int, k int) []int {
	frequencyTracker := make(map[int]int)
	rankedSlice := make([][]int, len(nums)+1)

	for _, number := range nums {
		if _, isThere := frequencyTracker[number]; isThere {
			frequencyTracker[number]++
			continue
		}
		frequencyTracker[number] = 1
	}

	for num, frequency := range frequencyTracker {
		rankedSlice[frequency] = append(rankedSlice[frequency], num)
	}

	result := make([]int, 0)

	for i := len(rankedSlice) - 1; i > 0; i-- {
		result = append(result, rankedSlice[i]...)
		if len(result) == k {
			break
		}
	}

	return result
}
