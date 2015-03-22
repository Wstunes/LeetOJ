__author__ = 'wangshuo'

# A -> 1
#  B -> 2
#  C -> 3
#  ...
#  Z -> 26
#  AA -> 27
#  AB -> 28

class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        res = 0
        for i in range(len(s) ):

            res += 26**i * ( ord(s[len(s) - 1 - i]) - 64)

        return res

s = Solution()
print s.titleToNumber("Z")