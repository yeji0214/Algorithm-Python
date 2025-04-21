arr = []

num = 2024
m = 1
new_num = num * m

while new_num <= 100000:
    arr.append(new_num)
    m += 1
    new_num = num * m

N = int(input())
if N in arr:
    print("Yes")
else:
    print("No")