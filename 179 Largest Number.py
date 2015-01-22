__author__ = 'wangshuo'


class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):

        for i in range(0,len(num),1):
            for j in range(i,len(num),1):
                if int(str(num[i])+str(num[j])) < int(str(num[j])+str(num[i])):
                    temp = num[i]
                    num[i] = num[j]
                    num[j] = temp

        resString = ""
        for item in num:
            resString += str(item)

        if int(resString) == 0:
            return "0"
        return resString





s = Solution()
print s.largestNumber([0,0])
