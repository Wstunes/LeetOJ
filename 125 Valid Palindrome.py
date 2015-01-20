__author__ = 'wangshuo'

class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):

        temp = ""
        for item in s:

            if (ord(item) >= 65 and ord(item) <= 90) or (ord(item) >= 97 and ord(item) <= 122) or (ord(item) >= 48 and ord(item) <= 57):
                temp += item


        temp = temp.lower()

        start = 0
        end = len(temp) - 1


        while start <= end:
            if temp[start] != temp[end]:
                return False
            else:
                start += 1
                end -=1
        return True

s = Solution()
print s.isPalindrome("aa")