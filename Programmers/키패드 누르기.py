def get_position(num): # 현재 숫자의 좌표를 반환하는 함수 (0은 예외 처리)
    if num == 0:
        return [3, 1]
    return [(num - 1) // 3, (num - 1) % 3]

def solution(numbers, hand):
    result = ''
    cl = [3, 0]
    cr = [3, 2]
    left_key = [1, 4, 7]
    right_key = [3, 6, 9]
    
    for n in numbers:
        if n in left_key:
            cl = get_position(n)
            result += 'L'
        elif n in right_key:
            cr = get_position(n)
            result += 'R'
        else:
            goal = get_position(n)
            l, r = abs(cl[0] - goal[0]) + abs(cl[1] - goal[1]), abs(cr[0] - goal[0]) + abs(cr[1] - goal[1])
            if r > l:
                cl = goal
                result += 'L'
            elif r < l:
                cr = goal
                result += 'R'
            else:
                if hand == "right":
                    cr = goal
                    result += 'R'
                else:
                    cl = goal
                    result += 'L'
                    
    return result

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))