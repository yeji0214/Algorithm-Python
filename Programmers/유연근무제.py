def solution(schedules, timelogs, startday):
    answer = 0
    
    for i in range(len(schedules)):
        p = 0
        day = startday
        
        time_str = str(schedules[i])
        if len(time_str) == 3:
            goal = int(time_str[0]) * 60 + int(time_str[1:])
        else:
            goal = int(time_str[:2]) * 60 + int(time_str[2:])
            
        for j in range(7):
            if day <= 5:
                current_str = str(timelogs[i][j])
                if len(current_str) == 3:
                    current = int(current_str[0]) * 60 + int(current_str[1:])
                else:
                    current = int(current_str[:2]) * 60 + int(current_str[2:])
            
                if current <= goal + 10:
                    p += 1
                    
            day += 1
            if day == 8:
                day = 1
        if p == 5:
            answer += 1
                
    return answer

print(solution(	[700, 800, 1100], [[710, 2359, 1050, 700, 650, 631, 659], [800, 801, 805, 800, 759, 810, 809], [1105, 1001, 1002, 600, 1059, 1001, 1100]], 5))