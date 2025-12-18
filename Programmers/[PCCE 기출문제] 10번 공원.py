def sitable(arr): # 앉을 수 있는 자리인지 확인
    for i in range(len(arr)):
        if arr[i].count('-1') != len(arr[i]):
            return False
    return True

def solution(mats, park):
    mats = sorted(mats, reverse=True)

    N, M = len(park), len(park[0])
    
    for m in mats:
        for i in range(N - m + 1):
            for j in range(M - m + 1):
                arr = [p[j:j+m] for p in park[i:i+m]]
                if sitable(arr):
                    return m         
    return -1