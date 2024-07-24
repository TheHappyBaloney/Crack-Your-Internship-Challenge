# 25. Reverse Nodes in k-Group

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        def reverse(first, last, pre_first):
            nonlocal head

            if pre_first:
                pre_first.next = last
            else:
                head = last

            prev, curr = first, first.next
            first.next = last.next

            for i in range(k - 1):
                curr.next, prev, curr = prev, curr, curr.next

        count = 1
        curr = first = head
        pre_first = None
        while curr:
            if count == k:
                
                reverse(first, curr, pre_first)
                pre_first = first
                curr, first = first.next, first.next
                count = 1
            else:
                curr = curr.next
                count += 1
        
        return head
