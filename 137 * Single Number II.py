#-*-coding:utf-8-*-


__author__ = 'wangshuo'


# 把数组中每个数的二进制每一位想加，然后模3，最终的数即为 single Number
# 注意结果可能是负数，负数的位运算很坑，所以先统计数组中所有负数的个数判断结果是不是负数



class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        negativeCount = 0
        for i in range(len(A)):
            if A[i] < 0:
                A[i] = - A[i]
                negativeCount += 1


        bitNum = [0 for i in range(64)]
        res = 0
        for i in range(32):
            for item in A:
                bitNum[i] += ( (item >> i) & 1 )

        for i in range(32):
            res = res | ( (bitNum[i] % 3) << i)

        if negativeCount % 3 == 1:
            res = -res

        return res




s = Solution()
print s.singleNumber([1,1,1,-5])