def solution(video_len, pos, op_start, op_end, commands):
    op_start_int = int(op_start.split(':')[0]) * 60 + int(op_start.split(':')[1])
    op_end_int = int(op_end.split(':')[0]) * 60 + int(op_end.split(':')[1])
    video_len_int = int(video_len.split(':')[0]) * 60 + int(video_len.split(':')[1])
    current_time = int(pos.split(':')[0]) * 60 + int(pos.split(':')[1])
    
    for c in commands:
        if op_start_int <= current_time < op_end_int:
            current_time = op_end_int
        if c == 'prev':
            current_time -= 10
            if current_time < 0:
                current_time = 0
        elif c == 'next':
            current_time += 10
            if current_time > video_len_int:
                current_time = video_len_int
                
    if op_start_int <= current_time < op_end_int:
            current_time = op_end_int
                
    m, s = format(current_time // 60, '02'), format(current_time % 60, '02')
    
    return f'{m}:{s}'