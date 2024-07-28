# 1290. Convert Binary Number in a Linked List to Integer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        def toList(head, l) :
            if head :
                l.append(head.val)
                if head.next :
                    toList(head.next, l)
                return l
            return []
        l = toList(head, [])
        n2 = sum([l[len(l) - i - 1] * 2 ** i for i in range(len(l))])
        return n2
