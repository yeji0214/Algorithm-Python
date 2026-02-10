A = int(input())
B = int(input())
C = int(input())

result = str(A * B * C)
dic = {str(i): 0 for i in range(10)}

for r in result:
    dic[r] += 1

print(*dic.values(), sep='\n')