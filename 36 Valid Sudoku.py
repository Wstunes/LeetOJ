__author__ = 'wangshuo'


def checkRow(board):
    for row in range(9):
        for num in range(9):
            if board[row].count(num+1) > 1:
                return False

    return True


def checkColumn(board):
    newBoard = []

    for row in range(9):
        tempArray = []
        for column in range(9):
            tempArray.append(board[column][row])

        newBoard.append(tempArray)
    for row in range(9):
        for num in range(9):
            if newBoard[row].count(num+1) > 1:
                return False

    return True


def checkBox(board):
    for row in [0,3,6]:
        for column in [0,3,6]:
            tempArray = []
            for r in range(row,row+3,1):
                for c in range(column,column+3,1):
                    tempArray.append(board[r][c])

            for num in range(9):
                if tempArray.count(num+1) > 1:
                    print tempArray
                    return False

    return True



class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        newBoard = []
        for item in board:
            temp = []
            for num in item:
                if num == ".":
                    temp.append(-1)
                else:
                    temp.append(int(num))

            newBoard.append(temp)


        #print checkBox(newBoard)
        return checkRow(newBoard)  and checkColumn(newBoard) and checkBox(newBoard)


s = Solution()
print s.isValidSudoku(["..5.....6","....14...",".........",".....92..","5....2...",".......3.","...54....","3.....42.","...27.6.."])



