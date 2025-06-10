N = int(input())
S = input()
result = {}

for s in S:
    if s == ' ' or s == ',' or s == '.':
        continue
    if s in result.keys():
        result[s] += 1
    else:
        result[s] = 1
        
print(list(v for k, v in result.items() if v == max(result.values()))[0])