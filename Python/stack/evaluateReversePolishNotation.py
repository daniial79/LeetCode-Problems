def eval_RPN(tokens: list[str]) -> int:
    stack = []
    
    for token in tokens:
        if token not in "+*/-":
            stack.append(token)
            continue
        
        right = int(stack.pop())
        left = int(stack.pop())
        
        match token:
            case "+":
                stack.append(str(left+right))
            case "*":
                stack.append(str(left * right))
            case "-":
                stack.append(str(left - right))
            case "/":
                stack.append(str(int(left / right)))                
        

        
    return int(stack.pop())

print(eval_RPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))