def two_sum(nums: list[int], target: int) -> list[int]:
    holder = {}
    for index, number in enumerate(nums):
        temp = target - number
        if holder.get(temp) is not None:
            return [index, holder.get(temp)]
        holder.setdefault(number, index)
    return []