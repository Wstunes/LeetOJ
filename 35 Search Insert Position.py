__author__ = 'wangshuo'

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        if target < A[0]:
            return 0
        elif target > A[-1]:
            return len(A)

        low = 0
        high = len(A)
        while low < high:
            mid = (low + high) / 2
            if target == A[mid]:
                return mid
            elif target < A[mid]:
                if target > A[mid -1]:
                    return mid
                else:
                    high = mid - 1
            else:
                 low = mid + 1

        return high





s = Solution()
print s.searchInsert([1,3],2)