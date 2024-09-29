"""
- node 클래스 만들어서 Trie만들어야하는지 자료구조 뭐쓰지?????? : 그 값 가장 작은거 최상단에 놔주는 큐 있었는데 뭐지 => 힙


1. 좌표 값에서 트리 구조 뽑아야 함
y값 같으면 같은 height, 이진트리니까 y값 큰것(2^0)부터 7[8,6] 
다음 y값 (2[11,5],4[3,5]) 여기서 x값 작으면 left side, 크면 right side  - y값 개수 체크 필요없이 그냥 같은 값인 애 다 찾으면 height에서의 개수 특징 만족할것
다음 y값 (1[5,3],3[13,3],6[1,3]) x값 6(1), 1(5), 3(13)
    - 완전 이진트리가 아닌케이스 (4개보다 노드 적음) -> 어떤 노드가 어디에 달려있는지 판별해야함
                    4(3)    2(11)
                6(1), 1(5),     3(13)
다음 y값 (8[7,2], 9[2,2]])
                6(1), 1(5),     3(13)
                    9(2)  8(7)
            근데 9가 1 자식이 아니라 6 자식인건 어케알지 -> 4를 봐야됨.....
    
[
        1[5,3],
    2[11,5],
        3[13,3],
    4[3,5],
                    5[6,1],
        6[1,3],
7[8,6],
            8[7,2],
            9[2,2]]
2. 트리에서 preorder, postorder
"""
class Node:
    def __init__(self, id, x, y) -> None:
        self.id = id
        self.x, self.y = x, y
        self.left, self.right = None, None

    def __lt__(self, other):
        if self.y == other.y:
            return self.x < other.x
        return self.y > other.y

def addNode(parent, child):
    if child.x < parent.x:
        if parent.left is None:
            parent.left = child
        else:
            addNode(parent.left, child)
    else:
        if parent.right is None:
            parent.right = child
        else:
            addNode(parent.right, child)

def preorder(ans, node):
    if node is None: return
    ans.append(node.id)
    preorder(ans, node.left)
    preorder(ans, node.right)

def postorder(ans, node):
    if node is None: return
    postorder(ans, node.left)
    postorder(ans, node.right)
    ans.append(node.id)
    

def solution(nodeinfo):
    n = len(nodeinfo)
    nodeList = []
    for i in range(n):
        nodeList.append(Node(i+1, nodeinfo[i][0], nodeinfo[i][1]))
    nodeList.sort()
    
    # 트리 만들기
    root = nodeList[0]
    for i in range(1, n):
        addNode(root, nodeList[i])

    # traversal
    answer = [[], []]
    preorder(answer[0], root)
    postorder(answer[1], root)

    return answer

ans = solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]])
print(ans)