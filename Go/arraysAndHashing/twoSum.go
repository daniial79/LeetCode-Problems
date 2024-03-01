package arraysAndHashing

func twoSum(nums []int, target int) []int {
	var result [2]int
	tracker := make(map[int]int)

	for idx1, num := range nums {
		complementary := target - num
		if idx2, isThere := tracker[complementary]; isThere {
			result[0], result[1] = idx2, idx1
			break
		}

		tracker[num] = idx1
	}

	return result[:]
}
