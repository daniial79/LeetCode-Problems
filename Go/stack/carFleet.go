package stack

import "sort"

func carFleet(target int, position []int, speed []int) int {
	pairs := make([]carInfo, 0)
	timeTracker := []float32{}

	for i := 0; i < len(position); i++ {
		pairs = append(pairs, carInfo{
			pos: position[i],
			spd: speed[i],
		})
	}

	sort.Slice(pairs, func(i, j int) bool {
		return pairs[i].pos < pairs[j].pos
	})

	for i := len(pairs) - 1; i >= 0; i-- {
		timeTracker = append(timeTracker, float32(target-pairs[i].pos)/float32(pairs[i].spd))
		if len(timeTracker) >= 2 && timeTracker[len(timeTracker)-1] <= timeTracker[len(timeTracker)-2] {
			timeTracker = timeTracker[:len(timeTracker)-1]
		}
	}

	return len(timeTracker)
}

type carInfo struct {
	pos int
	spd int
}
