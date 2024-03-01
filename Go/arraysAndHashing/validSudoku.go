package main

func isValidSudoku(board [][]byte) bool {
	for _, row := range board {
		if !validate(row) {
			return false
		}
	}

	for i := 0; i < 9; i++ {
		column := make([]byte, 0)
		for j := 0; j < 9; j++ {
			column = append(column, board[j][i])
		}
		if !validate(column) {
			return false
		}
	}

	for i := 0; i <= 6; i += 3 {
		for j := 0; j <= 6; j += 3 {
			if !validate(gridToSlice(board, i, j)) {
				return false
			}
		}
	}
	return true
}

func gridToSlice(board [][]byte, x, y int) []byte {
	bs := make([]byte, 0)
	for i := x; i < x+3; i++ {
		for j := y; j < y+3; j++ {
			bs = append(bs, board[j][i])
		}
	}

	return bs
}

func validate(bs []byte) bool {
	isThere := make(map[byte]bool)

	for _, b := range bs {
		if b == '.' {
			continue
		}

		if isThere[b] {
			return false
		}
		isThere[b] = true
	}

	return true
}
