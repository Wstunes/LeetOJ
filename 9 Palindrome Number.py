__author__ = 'wangshuo'


class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0 :
            return False
        if x == 0:
            return True

        base = 1
        while x / base >= 10:
            base *= 10


        while x:
            right = x % 10
            left = x / base

            if right != left:
                return False

            x %= base
            base /= 100
            x /= 10

        return True


s = Solution()
print s.isPalindrome(100001)
