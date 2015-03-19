#-*-coding:utf-8-*-

__author__ = 'wangshuo'

# 使用i和j两个指针进行搜索，i代表候选的最长子串的开头，j代表候选的最长子串的结尾。
# 先假设i不动，那么在理想的情况下，我们希望可以一直右移j，直到j到达原字符串的结尾，此时j-i就构成了一个候选的最长子串。每次都维护一个max_length，就
# 可以选出最长子串了。
# 实际情况是，不一定可以一直右移j，如果字符j已经重复出现过（假设在位置k），就需要停止右移了。记录当前的候选子串并和max_length做比较。接下来为下
# 一次搜寻做准备。
# 在下一次搜寻中，i应该更新到k+1。这句话的意思是，用这个例子来理解，abcdef是个不重复的子串，abcdefc中（为了方便记录为abc1defc2）,c1和c2重复了。那
# 么下一次搜寻，应该跨过出现重复的地方进行，否则找出来的候选串依然有重复字符，且长度还不如上次的搜索。所以下一次搜索，直接从c1的下一个字符d开始进
# 行，也就是说，下一次搜寻中，i应该更新到k+1。
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = 0
        end = 0
        maxLen = 0
        length = len(s)
        exist = {}
        for i in range(256):
            exist[i] = 0


        while end < length:

            if exist[ord(s[end])] == 0:
                exist[ord(s[end])] = 1
                end += 1
            else:
                maxLen = max(maxLen , end - start)


                # res = ""
                # for i in range(start,end,1):
                #     res += s[i]
                # print res


                while s[start] != s[end]:
                    exist[ord(s[start])] = 0
                    start += 1

                end += 1
                start += 1

        # print maxLen

        return max(maxLen,length - start )

s = Solution()
s.lengthOfLongestSubstring("abcabcbb")