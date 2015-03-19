#-*-coding:utf-8-*-
__author__ = 'wangshuo'



# �÷����ĺ����ǽ�ԭ����ת���һ��Ѱ�ҵ�kС�������⣨��������ԭ�����������У���������λ��ʵ�����ǵ�(m+n)/2С����������ֻҪ����˵�kС����
# ���⣬ԭ����Ҳ���Խ����
#
# ���ȼ�������A��B��Ԫ�ظ���������k/2�����ǱȽ�A[k/2-1]��B[k/2-1]����Ԫ�أ�������Ԫ�طֱ��ʾA�ĵ�k/2С��Ԫ�غ�B�ĵ�k/2С��Ԫ�ء�����
# ��Ԫ�رȽϹ������������>��<��=�����A[k/2-1]<B[k/2-1]�����ʾA[0]��A[k/2-1]��Ԫ�ض���A��B�ϲ�֮���ǰkС��Ԫ���С����仰˵��A[k/2-1]��
# ���ܴ���������ϲ�֮��ĵ�kСֵ���������ǿ��Խ���������
#
# ��A[k/2-1]=B[k/2-1]ʱ�������Ѿ��ҵ��˵�kС������Ҳ�������ȵ�Ԫ�أ����ǽ����Ϊm��������A��B�зֱ���k/2-1��Ԫ��С��m������m���ǵ�kС
# ������(���kΪ��������m������λ���������ǽ��������뻯���ǣ���ʵ�ʴ��������в�ͬ��������k/2��Ȼ������k-k/2�����һ������)
#
# ͨ������ķ��������Ǽ����Բ��õݹ�ķ�ʽʵ��Ѱ�ҵ�kС�������������ǻ���Ҫ���Ǽ����߽�������
#
# ���A����BΪ�գ���ֱ�ӷ���B[k-1]����A[k-1]��
# ���kΪ1������ֻ��Ҫ����A[0]��B[0]�еĽ�Сֵ��
# ���A[k/2-1]=B[k/2-1]����������һ����

class Solution:
    # @return a float


    def findKth(self,A,B,k):
        #always assume that m is equal or smaller than n
        if len(A) > len(B):
            return self.findKth(B,A,k)

        if len(A) == 0:
            return B[k - 1]
        if k == 0 or k == 1:
            return min(A[0],B[0])

        #divide k into two parts
        pa = min(len(A),k / 2)
        pb = k - pa
        if A[pa - 1] < B[pb - 1]:
            return self.findKth(A[pa :],B,k - pa)
        elif A[pa - 1] > B[pb - 1]:
            return self.findKth(A,B[pb :],k - pb)
        else:
            return A[pa - 1]
    def findMedianSortedArrays(self, A, B):
        totalLen = len(A) + len(B)
        if totalLen % 2 != 0:
            return self.findKth(A,B,totalLen / 2 + 1)
        else:
            return float((self.findKth(A,B,totalLen / 2 )) + self.findKth(A,B,totalLen / 2 + 1) ) / 2

a = Solution()

print a.findMedianSortedArrays([],[2,3])

