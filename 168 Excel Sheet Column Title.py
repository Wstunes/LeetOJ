#-*-coding:utf-8-*-

__author__ = 'wangshuo'

# 1 -> A
# 2 -> B
# 3 -> C
# ...
# 26 -> Z
# 27 -> AA
# 28 -> AB

# 10进制转26进制

class Solution:
    # @return a string
    def convertToTitle(self, num):
        res = ""
        n = num

        while(n):

            n -= 1
            res = chr(n%26 + ord('A')) + res

            n = n / 26
        return res





s= Solution()
print s.convertToTitle(28)