def is_valid(s: str) -> bool:
    stack = []
    for par in s:
        if is_closing(par):
            if len(stack) == 0:
                return False
            last_item = stack.pop()
            if not are_paired(last_item, par):
                return False
        else:
            stack.append(par) 
    return len(stack) == 0   
    
    
def is_closing(par: str) -> bool:
    if par in ["]", "}", ")"]:
        return True
    
def are_paired(opening: str, closing: str) -> bool:
    if opening == "(":
        return closing == ")"
    if opening == "[":
        return closing == "]"
    if opening == "{":
        return closing == "}"
    
        