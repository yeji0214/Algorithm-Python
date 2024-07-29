def solution(n):
    ans = ''
    ans += n // 2 * '수박'
    ans += n % 2 * '수'
    return ans