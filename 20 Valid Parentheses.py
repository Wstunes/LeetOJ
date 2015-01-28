__author__ = 'wangshuo'



class Solution:
    # @return a boolean
    def isValid(self, s):
        tempStack = []
        i = 0
        for c in s:
            tempStack.append(c)
            if len(tempStack) == 1:
                continue
            if (tempStack[i] == "(" and tempStack[i+1] == ")" ) or (tempStack[i] == "{" and tempStack[i+1] == "}" ) \
                    or (tempStack[i] == "[" and tempStack[i+1] == "]" ):
                tempStack.pop()
                tempStack.pop()
                if i != 0:
                    i -= 1

            elif tempStack[i] == ")" or tempStack[i] == "]" or tempStack[i] == "}":
                return False
            else:
                i += 1



        if len(tempStack) == 0:
            return True
        else:
            return False


s= Solution()
print s.isValid("(()([]){})")