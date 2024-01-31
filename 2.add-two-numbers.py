#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
"""
LL ; 두 개의 음이 아닌 정수 표현, 들어온 리스트에 대해 역순으로 저장됨
l1 = [2,4,3], l2 = [5,6,4]이게 들어왔을때
342 + 465 = 807 니까 [7,0,8] 를 리턴하기

- 일단 plain으로 풀어보기 (Linked List자료구조 없이)

## solution
1. create a placeholder
    - `dummyhead` = value of 0
    - hold the resulting LinkedList
2. initialize pointer `tail`, set it to `dummyhead`
    - keep track of the last node in the result list
3. initialize variable `carry`, set it to 0
    - store the carry value during adding calculation
4. loop
    - until there are no more digits in both l1, l2 and no remaining carry value
    - 1. current node of l1, l2
        - check if these are exists, assign to d1, d2 (ow, 0)
    - 2. sum = d1+d2+carry
        - sum%10 will be the current node V
        - sum/10 will be the updated carry value
    - 3. create a new node with V
    - 4. attach the new node to the tail node of the result list
    - 5. move the tail pointer to the newly added node
    - 6. nove to the next mnodes in both l1, l2
"""
# @lc code=start
from typing import Optional
# Optional : 타입힌트를 위해 사용되는 유틸리티
# Optional[X] : X 타입 또는 None 타입을 가질 수 있는 변수라는 점을 나타냄

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        """
        next는 ListNode, 즉 다음 노드의 Node객체가 들어오는것
        L1생성하면 얘는 맨 처음 노드만 쥐고있고 나머지는 알아서 꿰어있어야함
        """
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers_bf(self, l1: list, l2: list) -> list:
        """
        제출이 안됨 ㅎ
        문제에서 요구한 자료구조 사용하기
        """
        total = 0
        for i in range(len(l1)):
            total += l1[i] * (10**i)
        for i in range(len(l2)):
            total += l2[i] * (10**i)
        total = str(total)
        return [int(total[i]) for i in range(len(total)-1, -1, -1)]

    @staticmethod
    def make_LL(now, next): 
        """
        Linked List에서 다음 노드를 생성하고 포인터를 연결하는 재귀함수
        - now, next받아서 현재 노드 생성하고 next Linked List node 생성하고 현재 노드의 next로 할당
        - next가 None으로 들어오면 return
        """
        if next == None: return
            
        ListNode(now, ListNode())
        tmp = []
        for i in range(len(lst)-1):
            
            tmp.append(ListNode(lst[i], lst[i+1]))
        tmp.append(ListNode(lst[-1], None)) 

        L1 = ListNode()
        return tmp

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        l1 = [2,4,3], l2 = [5,6,4]이게 들어왔을때
        342 + 465 = 807 니까 [7,0,8] 를 리턴하기
        """
        dummyhead = ListNode()
        tail = dummyhead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            d1 = l1.val if l1 is not None else 0
            d2 = l2.val if l2 is not None else 0
            sum = d1 + d2 + carry
            d, carry = sum % 10, sum // 10

            newNode = ListNode(d)
            tail.next = newNode 
            tail = tail.next
            print(f"newNode: {newNode}\ntail: {tail}\nl1: {l1}, l2: {l2}\n\n")

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = dummyhead.next
        dummyhead.next = None
        return result



# @lc code=end

