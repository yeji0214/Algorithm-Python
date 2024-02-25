# 그리디
# 새로 알게 된 것: 포맷 연산자 %g ( 이 문제에선 불필요한 소수점 0을 지우기 위해 사용함. ex) 20.0 )
N = int(input())
drinks = sorted(list(map(int, input().split())))

for i in range(N-1):
    drinks[i] /= 2

print("%g" % (sum(drinks[0:N-1]) + drinks.pop()))