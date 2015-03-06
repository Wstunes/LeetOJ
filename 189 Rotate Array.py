__author__ = 'wangshuo'


class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        if k == 0:
            return

        step = k % len(nums)
        nums[:] = nums[-step :] + nums[ : -step]
        print nums



s = Solution()
s.rotate([1,2], 1)