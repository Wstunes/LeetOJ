__author__ = 'wangshuo'



class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binary = bin(n)[2:]
        zeroNum = 32 - len(binary)
        for i in range(zeroNum):
            binary = "0" + binary

        resBinary = ""
        for i in range(len(binary)):
            resBinary = resBinary + binary[len(binary) - 1 - i]


        return int(resBinary,2)





s = Solution()
s.reverseBits(43261596)
