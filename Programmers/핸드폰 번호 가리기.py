def solution(phone_number):
    ans = ''
    for n in range(len(phone_number) - 4):
        ans += '*'
    ans += phone_number[-4:]
    return ans