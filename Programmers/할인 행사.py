def solution(want, number, discount):
    buy = {}
    ans = 0
    
    for i in range(len(want)):
        buy[want[i]] = number[i]
        
    for i in range(len(discount) - 10 + 1):
        for name in buy:
            if buy[name] != discount[i:i+10].count(name):
                break
            if name == list(buy.keys())[-1]:
                ans += 1
    
    return ans

print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))