# def solution(today, terms, privacies):
#     terms_info = { k: int(v) for k, v in (item.split() for item in terms) }
#     answer = []
#     ty, tm, td = map(int, today.split('.'))
    
#     for i in range(len(privacies)):
#         s, e = privacies[i].split()
#         e = terms_info[e]
#         y, m, d = map(int, s.split('.'))
        
#         if d == 1:
#             e -= 1
#             next_date = 28
#         else:
#             next_date = d - 1
            
#         ny, nm, nd = y + (m + e - 1) // 12, (m + e - 1) % 12 + 1, next_date
        
#         pre = ty * 12 * 28 + tm * 28 + td
#         nxt = ny * 12 * 28 + nm * 28 + nd
        
#         if pre > nxt:
#             answer.append(i + 1)
    
#     return answer

def solution(today, terms, privacies):
    ans = []
    today_arr = list(map(int, today.split('.')))
    t = today_arr[0] * 336 + (today_arr[1] - 1) * 28 + today_arr[2]
    dict_terms = {}

    for term in terms:
        t1, t2 = term.split()
        dict_terms[t1] = int(t2)

    for i in range(len(privacies)):
        date, kind = privacies[i].split()
        y, m, d = list(map(int, date.split('.')))

        result_m = m + dict_terms[kind]
        if result_m > 12:
            y += result_m // 12
            m = result_m % 12
        else:
            m = result_m

        result = y * 336 + (m - 1) * 28 + d

        if t >= result:
            ans.append(i + 1)

    return ans

print(solution("2020.01.01"	, ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))