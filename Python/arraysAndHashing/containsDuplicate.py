def contains_duplicate(nums: list[int]) -> bool:
    existence_check = {}
    for num in nums:
        if existence_check.get(num):
            return True
        existence_check.setdefault(num, True)
    return False

def contains_duplicate_1(nums: list[int]) -> bool:
    return list(set(nums)) == nums