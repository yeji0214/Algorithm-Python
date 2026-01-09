def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    arr1 = []
    arr2 = []
    common = 0
    total = 0
    
    for i in range(len(str1) - 1):
        if 'a' <= str1[i] <= 'z' and 'a' <= str1[i + 1] <= 'z':
            arr1.append(str1[i] + str1[i + 1])
            
    for i in range(len(str2) - 1):
        if 'a' <= str2[i] <= 'z' and 'a' <= str2[i + 1] <= 'z':
            arr2.append(str2[i] + str2[i + 1])
            
    if len(arr1) == len(arr2) == 0:
        return 65536
            
    for a in arr1:
        if a in arr2:
            arr2.remove(a)
            common += 1
    total = len(arr1) + len(arr2)
    
    return int((common / total) * 65536)