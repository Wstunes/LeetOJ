__author__ = 'wangshuo'


class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        split1 = version1.split(".")
        split2 = version2.split(".")

        cursor = 0
        while cursor < len(split1) and cursor < len(split2):
            if int(split1[cursor]) < int(split2[cursor]):
                return -1
            elif int(split1[cursor]) > int(split2[cursor]):
                return 1
            else:
                cursor += 1

        if len(split1) == len(split2):
            return 0
        elif cursor == len(split1):
            for i in range(cursor,len(split2),1):
                if int(split2[i]) != 0:
                    return -1
            return 0
        elif cursor == len(split2):
            for i in range(cursor,len(split1),1):
                if int(split1[i]) != 0:
                    return 1
            return 0


s = Solution()
print s.compareVersion("10.6.5","10.6")
