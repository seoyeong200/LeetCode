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


### 트라이로 풀어보기
# Node 클래스 만드는게 나을지, 그냥 계속 중첩된 딕셔너리 구조로 가는게 나을지
# Node 클래스 만들어서 시도
from collections import defaultdict

class Node:
    def __init__(self) -> None:
        self.childs = {} # 알파벳: [노드]
        self.lens = defaultdict(int)

# def print__(root, height):
#     if root.childs == {}: return
#     for key, val in root.childs.items():
#         print(' '*height, key)
#         print__(val, height+1)
        
def addNode(root, word) -> Node:
    search = root
    w_len = len(word)
    for w in word:
        # 현재 노드에 새로운 알파벳 노드 추가 필요
        if w not in search.childs.keys():
            node = Node()
            search.childs[w] = node
        search.lens[w_len] += 1
        search = search.childs[w]
    return root

def find_cnt(trie: Node, query: str) -> int:
    search = trie
    for q in query:
        if q == '?': 
            print(query, search.childs.keys(), search.lens.items())
            return search.lens[len(query)]
        else: 
            if q not in search.childs.keys():
                return 0
            search = search.childs[q]

    return -1

def solution(words, queries):
    answer = []
    root = Node()
    rev_root = Node()
    for word in words:
        root = addNode(root, word)
        rev_root = addNode(rev_root, word[::-1])
    # print__(root, 0)
    # print__(rev_root, 0)
        
    for query in queries:
        # root 트리 이용
        if query[-1] == '?': 
            cnt = find_cnt(root, query)
        # rev_root 이용
        else:
            cnt = find_cnt(rev_root, query[::-1])
        answer.append(cnt)
    return answer
    

ans = solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"])
print(ans)