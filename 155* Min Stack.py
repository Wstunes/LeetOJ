#-*-coding:utf-8-*-
__author__ = 'wangshuo'


# 用两个stack来记录，其中一个stack是记录最小值的下标

class MinStack:
    # @param x, an integer
    # @return an integer
    def __init__(self):
        self.minIndexStack = list()
        self.stack = list()


    def push(self, x):
        self.stack.append(x)
        if len(self.minIndexStack) == 0 or x < self.stack[self.minIndexStack[-1]]:
            self.minIndexStack.append(len(self.stack) - 1)


    # @return nothing
    def pop(self):
        self.stack.pop()
        if self.minIndexStack[-1] == len(self.stack):
            self.minIndexStack.pop()

    # @return an integer
    def top(self):
        return self.stack[len(self.stack) - 1]

    # @return an integer
    def getMin(self):
        return self.stack[self.minIndexStack[-1]]
