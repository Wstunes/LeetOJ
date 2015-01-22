__author__ = 'wangshuo'



class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        timesDic = {}
        for item in num:
            if item in timesDic:
                timesDic[item] += 1
            else:
                timesDic[item] = 1

        l = len(num)
        lhalf = l/2
        for items in timesDic:
            if timesDic[items] > lhalf:
                return items

s = Solution()
print s.majorityElement([3,3,4])
