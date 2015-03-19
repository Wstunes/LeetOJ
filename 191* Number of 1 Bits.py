#-*-coding:utf-8-*-


__author__ = 'wangshuo'

# n = 0x110100    n-1 = 0x110011   n&(n - 1) = 0x110000
# n = 0x110000    n-1 = 0x101111   n&(n - 1) = 0x100000
# n = 0x100000    n-1 = 0x011111   n&(n - 1) = 0x0
# 新的解法，n中本来有3个1，按照此种思路只需要循环3此即可求出最终结果，比第一种暴力枚举的解法要少很多次




class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        count = 0
        while n != 0:
            n = n & (n - 1)
            count += 1

        return count