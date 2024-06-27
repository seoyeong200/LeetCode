#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional
"""
문제
left는 나보다 작고 right는 나보다 큰 value의 노드로 구성된 트리(BST)
next메소드를 호출하면 현재 value보다 크면서 가장 작은 원소 리턴하고
hasNext 메소드를 호출하면 해당 노드가 존재하는지를 리턴한다.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    """
    문제에서 요구하는 순서대로 노드들을 리스트에 넣고 하나씩 리턴해주는 방식
    리스트에 노드를 넣을때 왼쪽 traversal -> 현재 노드 -> 오른쪽 traversal 이런식으로 넣는다 [*traversal() 참고]
    인덱스 tracking하는 멤버변수 하나 만들어서 lst의 해당 인덱스에 있는 노드 리턴해준다.

    모든 노드를 다 리스트에 넣고 인덱스로 접근하다보니 time complexity는 많이 개선됐으나, space 효율이 떨어진다.
    """
    def __init__(self, root: Optional[TreeNode]) -> None:
        def traversal(node, lst):
            if node is None: return
            traversal(node.left, lst)
            lst.append(node)
            traversal(node.right, lst)

        self.lst = []
        traversal(root, self.lst)
        print(self.lst)

        self.idx = 0

    def next(self) -> int:
        node = self.lst[self.idx]
        self.idx+=1
        return node.val

    def hasNext(self) -> bool:
        return True if self.idx < len(self.lst) else False


class BSTIterator_mySolution:
    """ both time, space complextity are not efficient
    
    self.stk과 self.pushAll() 메소드를 둬서,
    self.pushAll() 의 argument로 준 노드를 시작 정점으로 스택에 traced node들을 넣으면서 left side traversal을 한다.
    hasNext는 자연스럽게 스택에 원소가 있는지의 여부로 판단하면 된다.
    next는 스택에서 원소를 하나 꺼내 right 노드를 pushAll()로 보내서 right 노드 기준으로 left depth 스택에 넣어주고 햔제 노드 val 리턴해주면 가능
    """
    def __init__(self, root: Optional[TreeNode]):
        """The pointer should be initialized to a non-existent number 
        smaller than any element in the BST
        make binary tree"""
        print(root)
        self.stk = []
        self.pushAll(root)

    def next(self) -> int:
        """Moves the pointer to the right, 
        then returns the number at the pointer."""
        tmp = self.stk.pop()
        if tmp.right is not None:
            self.pushAll(tmp.right)
        return tmp.val

    def hasNext(self) -> bool:
        """Returns true if there exists a number in the traversal to the right of the pointer, 
        otherwise returns false."""
        return bool(self.stk)

    def pushAll(self, node: Optional[TreeNode]):
        while node.val is not None:
            self.stk.append(node)
            node = node.left


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

