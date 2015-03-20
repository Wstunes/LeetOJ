__author__ = 'wangshuo'


class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        wordsList = s.split(" ")
        if len(wordsList) == 0:
            return 0
        else:
            for i in range(len(wordsList)):
                if wordsList[len(wordsList) - 1 - i] != "":
                    return len(wordsList[len(wordsList) - 1 - i])

        return 0

s = Solution()
print s.lengthOfLastWord("a ")

