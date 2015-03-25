#-*-coding:utf-8-*-

__author__ = 'wangshuo'

# 两个指针ptr1和ptr2，都从链表头开始走，ptr1每次走一步，ptr2每次走两步，等两个指针重合时，就说明有环，否则没有。如果有
# 环的话，那么让ptr1指向链表头，ptr2不动，两个指针每次都走一步，当它们重合时，所指向的节点就是环开始的节点


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        fast = head
        slow = head
        if not head:
            return None
        while fast:
            if fast.next == None:
                return None

            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                slow = head
                while fast != slow:
                    slow = slow.next
                    fast = fast.next

                return slow

        return None