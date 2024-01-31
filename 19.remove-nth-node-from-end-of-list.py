#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
"""
linked list의 head가 주어질 때 끝에서 n번째 노드를 제거하고 head리턴하기
"""

# @lc code=start
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def get_length(self, L):
        n = 1
        while L.next is not None:
            n+=1
            L = L.next
        return n
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        head에서부터 하나씩 건너가면서 현재 노드가 끝에서 n번째 노드라는걸 알기 위해선
        - 끝까지 가보는수밖에 없나..?
        - 각 노드 다 저장하는 리스트 하나 둬서 [n1, n2, n3, .. ] 한바퀴 다 돌면서 만들고 전체 길이 구한다음
        - len-n-1 인덱스에 있는 노드 포인터를 len-1번째 인덱스에 있는 노드로 연결하고
        - head 리턴하면 될라나?
        """
        dummyHead = ListNode(0)
        tail = dummyHead
        ll_len = self.get_length(head)

        idx = 1
        while True:
            if idx == ll_len-n+1:
                tail.next = head.next
                result = dummyHead.next
                dummyHead.next = None
                return result
            newNode = ListNode(head.val)
            tail.next = newNode
            tail = tail.next
            head = head.next
            idx+=1

# @lc code=end