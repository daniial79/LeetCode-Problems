def is_palindrome_v0(s: str) -> bool:
    left_pointer, right_pointer = 0, len(s) - 1
    
    while left_pointer <= right_pointer:
        left_char, right_char = s[left_pointer], s[right_pointer]
        
        if not left_char.isalnum():
            left_pointer += 1
            continue
        
        if not right_char.isalnum():
            right_pointer -= 1
            continue
        
        if left_char.isupper():
            left_char = left_char.lower()
            
        if right_char.isupper():
            right_char = right_char.lower()
            
        if left_char != right_char:
            return False
        
        left_pointer += 1
        right_pointer -= 1
        
    return True

def is_palindrome_v1(s: str) -> bool:
    mashed_string = ''.join(map(lambda x : x.lower() if x.isalpha() or x.isdigit() else '', s))
    length = len(mashed_string)
    return mashed_string[:(length - 1) // 2 + 1] == s[(length)//2:][::-1]