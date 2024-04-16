def two_sum(numbers: list[int], target: list[int]) -> list[int]:
    left, right = 0, len(numbers) - 1
    
    while left < right:
        candidate = numbers[left] + numbers[right]
        if candidate == target:
            return [left+1, right+1]
        elif candidate > target:
            right -= 1
        elif candidate < target:
            left += 1
            
    return []