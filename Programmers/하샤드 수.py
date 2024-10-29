def solution(x):
    h = sum(map(int, list(str(x))))
    if x % h == 0:
        return True
    return False