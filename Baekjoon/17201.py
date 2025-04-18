N = int(input())
A = input()
m = A[:2]

for i in range(1, N):
    si, ei = i * 2, i * 2 + 2
    if A[si:ei] != m:
        print("No")
        exit(0)
print("Yes")