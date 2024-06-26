#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
## second trial
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

""" input
TreeNode{val: 1, 
        left: TreeNode{val: 2, 
                        left: None, 
                        right: TreeNode{val: 5,    
                                        left: None, 
                                        right: None}}, 
        right: TreeNode{val: 3, 
                        left: None, 
                        right: TreeNode{val: 4, 
                                        left: None, 
                                        right: None}}}
"""
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        :root: Treenode instance
        각 height에서 rightmost node value 출력하는 문제
        len = n일때 bst 높이는 log2(n+1) 
        높이를 구할필요가 있나?/ 그냥 1번째, 1+2번째, 1+2+4번째.. 이런식으로
        """
        def queue_solution():
            """1. queue로 풀기"""
            from collections import deque
            q = deque([root])
            ans = []
            entire_vals = []

            while q: # 다음 탐색 노드 존재할때까지
                # find rightmost by queue
                print(f"q: {q}")
                s_node = q.popleft()
                entire_vals.append(s_node.val)
                if s_node.left:
                    q.append(s_node.left)
                if s_node.right:
                    q.append(s_node.right)
                
            print(entire_vals)

        def recursion_solution():
            """2. with recursion
            take arguments - node, level
            maintain result array, and result takes only the rightmost value at each level
            travasal right node first to update the rightmost value in result array
            """
            def recursion(node: TreeNode, level: int):
                print(f"node.val: {node.val if node is not None else None}, level: {level}")
                if node:
                    if len(ans) == level:
                        ans.append(node.val)
                    recursion(node.right, level+1)
                    recursion(node.left, level+1)
            
            ans = []
            recursion(root, 0)
            return ans


        return recursion_solution()

# @lc code=end



## first trial
# efinition for a binary tree node.
class TreeNode_tmp:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution_tmp:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        q = deque([root])
        ans = []
        lv = 0
        avail_nodes = 1
        while q:
            print(f"while loop with q {q}")
            # if child node is None, there's no more depth in next level from that node
            n = 2**avail_nodes
            avail_nodes = 0
            print(f"iterate {n} times")
            for i in range(n):
                prev = q.popleft(); print(f"prev : {prev}")
                if prev is not None:
                    rightmost = prev.val
                    q.append(prev.left)
                    q.append(prev.right)
                    avail_nodes +=1
            print(f"avail_nodes in the next level {avail_nodes}. appended q is {q}\n")
                    
            ans.append(rightmost)
            lv+=1
        return ans



"""
deque([TreeNode{val: 1, 
                left: TreeNode{val: 2, left: None, right: TreeNode{val: 5, left: None, right: None}}, 
                right: TreeNode{val: 3, left: None, right: TreeNode{val: 4, left: None, right: None}}
                }])
0 []
deque([TreeNode{val: 2, 
                left: None, 
                right: TreeNode{val: 5, 
                                left: None, 
                                right: None}}, 
        TreeNode{val: 3, 
                left: None, 
                right: TreeNode{val: 4, 
                                left: None, 
                                right: None}}])
1 [1]
deque([None, 
    TreeNode{val: 5, 
            left: None, 
            right: None},
    None, 
    TreeNode{val: 4, 
            left: None, 
            right: None}])
2 [1, 3]
deque([None, None, None, None])
"""