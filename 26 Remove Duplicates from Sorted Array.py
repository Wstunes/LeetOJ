__author__ = 'wangshuo'


class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):

        # for i in range(0,len(A),1):
        #     for k in range(i+1,len(A),1):
        #
        #         if k == len(A) - 1:
        #             A[i:k+1] = A[i:i+1]
        #             break
        #
        #         if A[i] == A[k]:
        #             continue
        #         else:
        #             A[i:k] = A[i:i+1]
        #             break
        if not A:
          return 0
        else:
            ii,jj=1,1
            while jj<len(A):
                if A[ii-1]!=A[jj]:
                    A[ii]=A[jj]
                    ii+=1
                jj+=1


            return ii






s =Solution()
s.removeDuplicates([1,1,2])
