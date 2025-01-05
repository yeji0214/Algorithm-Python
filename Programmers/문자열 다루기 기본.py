def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False
    
    for S in s:
        if S < '0' or S > '9':
            return False
        
    return True