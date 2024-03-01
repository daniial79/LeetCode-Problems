package stack

type node struct {
	value int
	rear  *node
}

func newNode(v int) node {
	return node{
		value: v,
		rear:  nil,
	}
}

type minimumTrackerStack []int

func (mts *minimumTrackerStack) push(value int) {
	*mts = append(*mts, value)
}

func (mts *minimumTrackerStack) pop() {
	*mts = (*mts)[:len(*mts)-1]
}

func (mts *minimumTrackerStack) get() int {
	return (*mts)[len(*mts)-1]
}

type MinStack struct {
	top            *node
	minimumTracker minimumTrackerStack
	depth          int
}

func Constructor() MinStack {
	return MinStack{
		top:            nil,
		depth:          0,
		minimumTracker: nil,
	}
}

func (this *MinStack) Push(val int) {
	generatedNode := newNode(val)

	if this.depth == 0 {
		this.top = &generatedNode
		this.depth++

		this.minimumTracker.push(val)

		return
	}

	generatedNode.rear = this.top
	this.top = &generatedNode
	this.depth++

	if this.minimumTracker.get() >= val {
		this.minimumTracker.push(val)
	}
}

func (this *MinStack) Pop() {
	if this.depth == 0 {
		return
	}

	head := this.top

	if head.value == this.minimumTracker.get() {
		this.minimumTracker.pop()
	}

	this.top = head.rear
	head.rear = nil
	this.depth--
}

func (this *MinStack) Top() int {
	return this.top.value
}

func (this *MinStack) GetMin() int {
	return this.minimumTracker.get()
}

/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */
