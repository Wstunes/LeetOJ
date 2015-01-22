__author__ = 'wangshuo'


class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        res = 0
        i = 5
        while n/i:
            res += n/i
            i = i*5
        return res