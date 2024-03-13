class Node:
    def __init__(self, value: int):
        self.value = value
        self.rear = None

class MinStack:
    def __init__(self):
        self.pointer = None
        self.minimumTracker = []
        self.depth = 0

    def getMin(self) -> int:
        return self.minimumTracker[-1]
    
    def push(self, val: int) -> None:
        generated_node = Node(val)
        
        if self.depth == 0:
            self.pointer = generated_node
            self.minimumTracker.append(val)
            self.depth += 1
            return None
        
        generated_node.rear = self.pointer
        self.pointer = generated_node
        self.depth += 1
        
        if self.getMin() >= val:
            self.minimumTracker.append(val)


    def pop(self) -> None:
        if self.depth == 0:
            return None
        
        
        head = self.pointer
        self.pointer = self.pointer.rear        
        head.rear = None
        self.depth -= 1
        
        if head.value == self.getMin():
            self.minimumTracker.pop()
        

    def top(self) -> int:
        return self.pointer.value

my_stack = MinStack()

my_stack.push(-2)

my_stack.push(0)

my_stack.push(-3)

my_stack.getMin()

my_stack.pop()

my_stack.top()

my_stack.getMin