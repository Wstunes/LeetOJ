__author__ = 'wangshuo'


class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        finalList = []

        for i in range(numRows):
            tempList = []
            for j in range(i+1):
                if j == 0 or j == i:
                    tempList.append(1)
                else:
                    tempList.append(finalList[i-1][j-1] + finalList[i-1][j])

            finalList.append(tempList)


        return finalList

s = Solution()
print s.generate(5)