# 구현, 브루트포스
def onoff(nX):
    global result
    ans = 0
    
    if nX < 1 or nX > N:
        return
    
    currentX = list(f'{X:0{K}d}')
    currentnX = list(f'{nX:0{K}d}')

    for i in range(K):
        currentXNum = num[currentX[i]].copy()
        currentnXNum = num[currentnX[i]].copy()
        common_values = [value for value in currentXNum if value in currentnXNum]
        final = [x for x in currentXNum + currentnXNum if x not in common_values]

        ans += len(final)

    if 0 < ans <= P:
        result += 1

# N: 최대 층수, K: 자리 수, P: 최대 반전 가능 수, X: 현재 층수
N, K, P, X = map(int, input().split())
num = {'0': [1,2,3,5,6,7], '1': [3,6], '2': [1,3,4,5,7], '3': [1,3,4,6,7], '4': [2,3,4,6], '5': [1,2,4,6,7], '6': [1,2,4,5,6,7], '7': [1,3,6], '8': [1,2,3,4,5,6,7], '9': [1,2,3,4,6,7]}
result = 0

for n in range(1, N+1):
    onoff(n) # 변경 대상 층수

print(result)