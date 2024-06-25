# 그리디
expression = input().split('-')
arr = []

for i in expression:
    num = 0
    for j in i.split('+'):
        num += int(j)
    arr.append(num)

result = arr[0]

for i in range(1, len(arr)):
    result -= arr[i]

print(result)