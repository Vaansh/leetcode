# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        tmp = []
        for l in lists:
            while l:
                tmp.append(l.val)
                l = l.next
        tmp.sort(reverse=True)

        res = None
        for t in tmp:
            res = ListNode(t, res)
        return res
