def group_anagrams(strs: list[str]) -> list[list[str]]:
    buckets = {}
    for string in strs:
        key = eval_key(string)
        if buckets.get(key):
            buckets[key].append(string)
        else:
            buckets[key] = [string]
    return list(buckets.values())


def eval_key(string: str) -> str:
    result = [0] * 26
    for char in string:
        result[ord(char) - ord('a')] += 1
    return str(result)
