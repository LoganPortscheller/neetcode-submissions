import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        linked_list_heap = []

        # it used to keep interpreter from comparing nodes with same priority
        it = 0
        # Push all linked list heads into a min heap
        for linked_list_head in lists:
            if linked_list_head:
                heapq.heappush(linked_list_heap, (linked_list_head.val, it,      
                    linked_list_head))

            it += 1


        head_merged_linked_list = None
        merged_linked_list_ptr = None

        while linked_list_heap:
            # Pop next node from min heap
            _, it, next_node = heapq.heappop(linked_list_heap)

            # Add to merged_linked_list
            if head_merged_linked_list:
                merged_linked_list_ptr.next = next_node
            else:
                head_merged_linked_list = next_node

            # Readd linked list to heap if there's more nodes
            next_in_linked_list = next_node.next
            if next_in_linked_list:
                heapq.heappush(linked_list_heap, (next_in_linked_list.val, it, next_in_linked_list))

            # next_node is no longer part of original linked list
            next_node.next = None

            merged_linked_list_ptr = next_node

        return head_merged_linked_list

            


        