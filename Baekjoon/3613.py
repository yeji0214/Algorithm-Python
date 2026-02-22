name = input().strip()
res = ''

if ('_' in name and name != name.lower()) or name[0] == '_' or name[-1] == '_' or '__' in name:
    print("Error!")
    exit(0)
if '_' in name: # C++
    words = name.split('_')
    res = words[0]

    for i in range(1, len(words)):
        if len(words[i]) <= 1:
            res += words[i][0].upper()
        else:
            res += words[i][0].upper() + words[i][1:]

elif name != name.lower(): # Java
    if name[0].isupper():
        print("Error!")
        exit(0)
    for n in name:
        if n == n.upper():
            res += f'_{n.lower()}'
        else:
            res += n
else:
    print(name)
    exit(0)

print(res)