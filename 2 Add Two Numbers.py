__author__ = 'wangshuo'


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):


        list = ListNode(0)
        head = list
        carry = 0

        while l1 or l2  or carry:
            l1val = 0
            l2val = 0
            if l1 :
                l1val = l1.val
                l1 = l1.next

            if l2 :
                l2val = l2.val
                l2 = l2.next

            sum = l1val + l2val

            if carry:
                sum += 1

            if sum > 9:
                carry = 1
                sum -= 10
                head.next = ListNode(sum)
                head = head.next
            else:
                carry = 0
                head.next = ListNode(sum)
                head = head.next

        return list.next
