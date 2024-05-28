# Definition for a binary tree node.

"""
[ Description ]
binary tree 주어지고 각 노드 주어질때 각 depth에서 가장 오른쪽 노드(rightmost node of each level) 리턴
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []


[ Solution ]
- use queue
- iterate over each level of the tree
    - each level, track the number of nodes in that level
    - traverse those nodes
        - update a variable prev with the value of the current node
        = prev value will be the rightmost value after finish each level
        - append to the answer
    - finish the loop when all levels are processed and the q is empty

"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = [root]
        ans = []
        lv = 0
        while q:
            if lv == 0: pass
            for _ in range(2**lv):
                prev = q.pop()
                rightmost = prev.val
                if prev is not None:
                    q.append(prev.left)
                    q.append(prev.right)
            ans.append(rightmost)
            lv+=1
            print(ans)
