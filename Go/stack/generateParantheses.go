package stack

import "strings"

func generateParenthesis(n int) []string {
	result := make([]string, 0)
	stack := make([]string, 0)

	var backtrack func(int, int)
	backtrack = func(left int, right int) {
		if left == n && right == n && right == left {
			result = append(result, strings.Join(stack, ""))
			return
		}

		if left < n {
			stack = append(stack, "(")
			backtrack(left+1, right)
			pop(&stack)
		}

		if left < right {
			stack = append(stack, ")")
			backtrack(left, right+1)
			pop(&stack)
		}
	}

	backtrack(0, 0)
	return result
}

func pop(list *[]string) {
	*list = (*list)[:len(*list)]
}
