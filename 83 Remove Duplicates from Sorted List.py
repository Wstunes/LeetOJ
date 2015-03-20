__author__ = 'wangshuo'


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        res = head
        current = head

        while current:
            if current.next == None:
                return res

            if current.next.next == None:
                if current.next.val == current.val:
                    current.next = None
                    return res
                else:
                    return  res

            if current.next.val == current.val:
                current.next = current.next.next

            else:
                current = current.next



