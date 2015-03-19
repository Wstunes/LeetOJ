#-*-coding:utf-8-*-

__author__ = 'wangshuo'


#每个数异或一遍，剩下的那个数就是要找的，因为两个相同的数异或以后是0

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):

        res = A[0]
        for i in range(len(A) - 1):
            res = res ^ A[i+1]

        return res

s = Solution()
s.singleNumber([1,1,2,2,3])

