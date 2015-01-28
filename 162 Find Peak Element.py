__author__ = 'wangshuo'



class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        if len(num) == 1:
            return 0
        if len(num) == 2:
            if num[0] > num[1]:
                return 0
            else:
                return 1
        for i in range(1,len(num) - 1):
            if num[i] > num[i-1] and num[i] > num[i+1]:
                return i

        if num[0] > num[1]:
            return 0
        elif num[-1] > num[len(num) - 2]:
            return len(num) -1


s = Solution()
print s.findPeakElement([1,2,3])