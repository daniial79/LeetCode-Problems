package stack

type stack []string

func (s *stack) push(char string) {
	(*s) = append(*s, char)
}

func (s *stack) pop() string {

	if len(*s) == 0 {
		return ""
	}

	popedChar := (*s)[len(*s)-1]

	*s = (*s)[0 : len(*s)-1]

	return popedChar
}

func isValid(s string) bool {
	initialstack := new(stack)

	for tapeHead := 0; tapeHead < len(s); tapeHead++ {
		currentChar := string(s[tapeHead])

		if isClosing(currentChar) {
			if len(*initialstack) == 0 {
				return false
			}

			lastPar := initialstack.pop()
			if !arePaired(lastPar, currentChar) {
				return false
			}
		} else {
			initialstack.push(currentChar)
		}
	}

	return len(*initialstack) == 0
}

func isClosing(par string) bool {
	return par == ")" || par == "]" || par == "}"
}

func arePaired(openingPar, closingPar string) bool {
	if openingPar == "(" {
		return closingPar == ")"
	}

	if openingPar == "{" {
		return closingPar == "}"
	}

	if openingPar == "[" {
		return closingPar == "]"
	}

	return false
}
