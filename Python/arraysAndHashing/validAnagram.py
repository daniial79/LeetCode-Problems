def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    alphabet_tracker = {}
    
    # initiating the alphabet tracker using first string
    for char in s:
        if not alphabet_tracker.get(char):
            alphabet_tracker.setdefault(char, 1)
        else:
            alphabet_tracker[char] += 1

    # removing alphabets of second string from alphabet tracker
    for char in t:
        if not alphabet_tracker.get(char):
            return False
        
        alphabet_tracker[char] -= 1
        if alphabet_tracker[char] == 0:
            del alphabet_tracker[char]

    # check if the alphabet tracker is empty
    return len(alphabet_tracker) == 0
        