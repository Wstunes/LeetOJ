__author__ = 'wangshuo'


class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):


        if digits[len(digits) - 1] + 1 < 10:
            digits[len(digits) - 1] += 1
            return digits
        else:
            digits[len(digits) - 1] = (digits[len(digits) - 1] + 1 ) % 10
            carry = 1

            if len(digits) - 2 >= 0:
                i = len(digits) - 2
            else:
                if digits[0] == 0:
                    digits.insert(0,1)
                    return digits

            while i :
                if digits[i] + carry >= 10:
                    digits[i] = ( digits[i]  + carry ) % 10
                    i -= 1
                else:
                    digits[i] = digits[i] + carry
                    return digits

            if digits[0] + carry >= 10:
                digits[0] = ( digits[0]  + carry ) % 10
                digits.insert(0,1)
                return digits
            else:
                digits[0] = digits[0]  + carry
                return digits


s= Solution()
print s.plusOne([9])