__author__ = 'wangshuo'


class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        while A.count(elem)>0:
            A.remove(elem)
        return len(A)

s = Solution()
print s.removeElement([4,5],4)