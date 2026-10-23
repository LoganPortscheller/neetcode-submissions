# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        tail = head

        nodes = list()

        while tail.next:
            nodes.append(tail)
            tail = tail.next

        while head != tail and head.next != tail:
            next_head = head.next
            
            head.next = tail
            tail.next = next_head

            head = next_head
            tail = nodes.pop()
        else:
            tail.next = None
