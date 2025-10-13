A, B = map(int, input().split())
C, D = map(int, input().split())

h = A + C
y = B + D
if h < y:
    print("Hanyang Univ.")
elif h == y:
    print("Either")
else:
    print("Yongdap")