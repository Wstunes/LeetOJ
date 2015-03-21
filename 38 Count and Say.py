__author__ = 'wangshuo'


class Solution:
    # @return a string
    def countAndSay(self, n):
        count = 1
        basic = "1"
        res = basic
        while count != n:
            tempRes = ""
            tempCount = 0
            for i in range(len(basic)):
                tempNum = basic[i]
                tempCount += 1
                if i+1 == len(basic) or basic[i] != basic[i+1]:
                    tempRes += str(tempCount) + tempNum
                    tempCount = 0

            count += 1
            basic = tempRes
            res = tempRes




        return res


s = Solution()
print s.countAndSay(5)