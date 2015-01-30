__author__ = 'wangshuo'


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):

        curA = headA
        curB = headB
        lenA = 0
        lenB = 0

        while curA:
            lenA += 1
            curA = curA.next

        while curB:
            lenB += 1
            curB = curB.next

        curA = headA
        curB = headB

        if lenA > lenB:
            for i in range(lenA - lenB):
                curA = curA.next
        elif lenB > lenA:
            for i in range(lenB - lenA):
                curB = curB.next

        while curA and curB:
            if curA == curB:
                return curA

            curA = curA.next
            curB = curB.next

        return None


s = Solution()
print s.getIntersectionNode({1},{1})