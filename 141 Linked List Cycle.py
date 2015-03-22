#-*-coding:utf-8-*-
__author__ = 'wangshuo'


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#解法1： 每到一个节点把该节点的 next 弄成头，判断下一个节点的 next 的 next是不是头，如果是则有环
class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        first = head
        if not head:
            return False
        while head:
            temp = head.next
            head.next = first
            head = temp
            if not temp or not temp.next :
                return False
            if temp.next.next == first:
                return True

        return False


#解法2：一个快指针 fast，一次跳两下，一个慢指针 slow 一次跳一下，如果有环，则两指针会相遇，如果 fast 走到末尾则没有环
class Solution1:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if not head:
            return False
        fast = head.next
        slow = head
        while fast:
            if fast.next == None:
                return False
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next

        return False
