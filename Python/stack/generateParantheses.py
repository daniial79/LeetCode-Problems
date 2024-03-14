def generate_parenthesis(n: int) -> list[str]:
    result = []
    
    def dfs(left: int, right: int, cargo: str) -> None:
        if left == 0 and right == 0:
            result.append(cargo)
        if left > 0:
            dfs(left - 1, right, cargo + "(")
        if left < right:
            dfs(left, right - 1, cargo + ")")
        
    dfs(n, n, "")
    return result