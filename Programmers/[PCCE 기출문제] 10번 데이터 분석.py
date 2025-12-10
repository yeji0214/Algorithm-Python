def solution(data, ext, val_ext, sort_by):
    idx = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    
    result = sorted([d for d in data if d[idx[ext]] < val_ext], key=lambda x: x[idx[sort_by]])
    
    return result