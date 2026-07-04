def solution(video_len, pos, op_start, op_end, commands):
    def to_sec(time):
        m, s = map(int, time.split(":"))
        return m * 60 + s
    
    def to_time(sec):
        m = sec // 60
        s = sec % 60
        return f"{m:02d}:{s:02d}"
    
    video_len = to_sec(video_len)
    pos = to_sec(pos)
    op_start = to_sec(op_start)
    op_end = to_sec(op_end)
    
    def op_skip(pos):
        if op_start <= pos <= op_end:
            return op_end
        return pos
    
    pos = op_skip(pos)
    
    for command in commands:
        if command == "prev":
            pos = max(0, pos - 10)
        else:
            pos = min(video_len, pos + 10)
            
        pos = op_skip(pos)
        
    return to_time(pos)