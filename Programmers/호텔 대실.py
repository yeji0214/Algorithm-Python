def solution(book_time):
    time = []
    room = []
    
    for b in book_time:
        s_t = list(map(int, b[0].split(':')))
        e_t = list(map(int, b[1].split(':')))
        
        time.append([s_t[0] * 60 + s_t[1], e_t[0] * 60 + e_t[1]])
        
    time = sorted(time, key=lambda x: x[0])

    for t in time:
        # 들어갈 수 있는 방의 인덱스를 가져오기
        available = [i for i in range(len(room)) if t[0] - 10 >= room[i]]
        
        if not available:
            room.append(t[1])
        else:
            # 가능한 애들 중 가장 빨리 종료되는 방으로
            idx = min(available, key=lambda i: room[i])
            room[idx] = t[1]
            
    return len(room)