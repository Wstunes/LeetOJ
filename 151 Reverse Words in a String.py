__author__ = 'wangshuo'


class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):

        temp = s.split(" ")
        ftemp = []
        for item in temp:
            if item != "":
                ftemp.append(item)
        res = ""
        if len(ftemp) > 0 :
            for i in range(0,len(ftemp) - 1,1):
                res += ftemp[len(ftemp) - i - 1]
                res += " "

            res += ftemp[0]
        return res



# s = Solution()
# print s.reverseWords("the sky is blue")
print  "    1     a".split(" ")
s = Solution()
print s.reverseWords(" ")