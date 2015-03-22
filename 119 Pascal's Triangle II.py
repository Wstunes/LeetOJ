__author__ = 'wangshuo'


class Solution:
    # @return a list of lists of integers
    def getRow(self, rowIndex):
        finalList = []

        for i in range(rowIndex + 1):
            tempList = []
            for j in range(i+1):
                if j == 0 or j == i:
                    tempList.append(1)
                else:
                    tempList.append(finalList[i-1][j-1] + finalList[i-1][j])

            finalList.append(tempList)


        return finalList[rowIndex]

s = Solution()
print s.getRow(3)