def solution(files):
    import re
    
    processed = []
    for i, file in enumerate(files):
        head_idx = re.match(r"[a-zA-Z\s.-]+", file).span()
        head = file[head_idx[0]:head_idx[1]].lower()
        
        remain = file[head_idx[1]:]
        num_idx = re.match(r"[0-9]+", remain).span()
        num = int(remain[num_idx[0]:num_idx[1]])
        
        processed.append([head, num, i, file])
        
    processed.sort(key=lambda x: (x[0], x[1], i))

    return [p[-1] for p in processed]