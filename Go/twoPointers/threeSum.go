package twoPointers

import "sort"

func ThreeSum(nums []int) [][]int {
	sort.Ints(nums)
	result := make([][]int, 0)

	for i, n := range nums {
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}

		l, r := i+1, len(nums)-1

		summation := n + nums[l] + nums[r]
		if summation == 0 {
			result = append(result, []int{n, nums[l], nums[r]})

			l++
			r--

			for nums[r] == nums[r+1] && l < r {
				r--
			}

			for nums[l] == nums[l-1] && l < r {
				l++
			}
		} else if summation > 0 {
			r--
		} else {
			l++
		}
	}

	return result
}
