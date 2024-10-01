def solution(words, queries):
    """
    키워드 : ?포함된 패턴 형태 문자열
        - ? : 글자 하나, 어떤 문자든 매치 (fro?? = (frodo, front, frost), fro?? != [frame, frozen])
    queries 키워드 배열 내 키워드 별로 매치된 단어 개수 리턴
    words ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries
    ["fro??",->  "frodo", "front", "frost" -> 3
    "????o", -> "frodo", "kakao" -> 2
    "fr???", "fro???", "pro?"]..
    
    fro?? => fro.{2}
    """
    import re
    
    answer = []
    visited = {}
    for q in queries:
        # create pattern string
        query = q.split('?')
        if q[-1] == '?': 
            pattern = '%s.{%d}$' %(query[0], len(query)-1)
        else: 
            pattern = '.{%d}%s$' %(len(query)-1, query[-1])   
            
        # find pattern matched words
        if pattern not in visited.keys():
            cnt = 0
            for word in words:
                if re.match(r"%s" %(pattern), word):
                    cnt+=1
            visited[pattern] = cnt
        else:
            cnt = visited[pattern]
            
        answer.append(cnt)
            
    return answer