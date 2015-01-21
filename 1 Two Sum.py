__author__ = 'wangshuo'


class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        head = 0
        tail = len(num) - 1
        indexList = []
        for i in range(0,len(num),1):
            indexList.append((num[i],i))


        num = sorted(num)

        while head < tail:
            if num[head] + num[tail] == target:
                for item in indexList:
                    if item[0] == num[head]:
                        index1 = item[1]
                for item in indexList:
                    if item[0] == num[tail] and index1 != item[1]:
                        index2 = item[1]

                if index1 < index2:
                    return (index1 + 1,index2 + 1)
                else:
                    return (index2 + 1,index1 + 1)

            elif num[head] + num[tail] < target:
                head += 1
            elif num[head] + num[tail] > target:
                tail -= 1

s = Solution()
print s.twoSum([0,4,3,0],0)