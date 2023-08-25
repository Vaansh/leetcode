# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        reorder = []
        length = 0
        while head:
            reorder.append(head)
            head = head.next
            length += 1

        l, r = 0, length - 1
        last = head
        while l < r:
            reorder[l].next = reorder[r]
            l += 1
            if l == r:
                last = reorder[r]
                break
            reorder[r].next = reorder[l]
            r -= 1
            last = reorder[l]
        if last:
            last.next = None
