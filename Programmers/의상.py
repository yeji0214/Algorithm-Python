def solution(clothes):
    clothes_dict = {}
    ans = 1
    
    for c in clothes:
        name, category = c[0], c[1]
        if category in clothes_dict:
            clothes_dict[category].append(name)
        else:
            clothes_dict[category] = [name]
            
    for k in clothes_dict:
        ans *= (len(clothes_dict[k]) + 1)
        
    return ans - 1