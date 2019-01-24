# lab27_Connect_Four.py
#still need to make sure entry is valid, tie games,


class Game:
    def __init__(self):
        self.board = [["|1|", "|2|", "|3|", "|4|", "|5|", "|6|", "|7|"],
                      ["| |", "| |", "| |", "| |", "| |", "| |", "| |"],
                      ["| |", "| |", "| |", "| |", "| |", "| |", "| |"],
                      ["| |", "| |", "| |", "| |", "| |", "| |", "| |"],
                      ["| |", "| |", "| |", "| |", "| |", "| |", "| |"],
                      ["| |", "| |", "| |", "| |", "| |", "| |", "| |"],
                      ["| |", "| |", "| |", "| |", "| |", "| |", "| |"]]

    def representation(self):
        for i in range(len(self.board)):
            print(''.join(self.board[i]))

    def placement(self, column, player):
        if self.board[1][column - 1] == "| |":
           # print(column)
            for i in range(6, 0, -1):
                if self.board[i][column - 1] == "| |":
                    self.board[i][column - 1] = player
                    self.representation()
                    if self.check_for_winner(i, column - 1) == "Winner":
                        print("Winner winner winner")
                        return "game_over"
                    else:
                        return 'continue'


    def check_for_winner(self, row, column):
        #check vertical, only need to count going down, we are looking from where we last placed, there wont be tiles on top yet
        print(row)
        print(column)
        while True:
            if row + 3 <= 6:
                count = 1
                for i in range(1, 4):
                    if self.board[row + i][column] == self.board[row][column]:
                        count += 1
                        if count == 4:
                            return "Winner"
            #check diagonal /
            topR_bottomL = 1
            if (row - 1 > 0) and (column + 1 <= 6) and (self.board[row - 1][column + 1] == self.board[row][column]):
                topR_bottomL += 1
                if (row - 2 > 0) and (column + 2 <= 6) and self.board[row - 2][column + 2] == self.board[row][column]:
                    topR_bottomL += 1
                    if (row - 3 > 0) and (column + 3 < 6) and self.board[row - 3][column + 3] == self.board[row][column]:
                        topR_bottomL += 1
            if (row + 1 <= 6) and (column - 1 >= 0) and (self.board[row + 1][column - 1] == self.board[row][column]):
                topR_bottomL += 1
                if (row + 2 <= 6) and (column - 2 >= 0) and (self.board[row + 2][column - 2] == self.board[row][column]):
                    topR_bottomL += 1
                    if (row + 3 <= 6) and (column - 3 >= 0) and (self.board[row + 3][column - 3] == self.board[row][column]):
                        topR_bottomL += 1
            if topR_bottomL >= 4:
                return "Winner"
            # check diaganal \
            topL_bottomR = 1
            if (row - 1 > 0) and (column - 1 >= 1) and (self.board[row - 1][column - 1] == self.board[row][column]):
                topL_bottomR += 1
                if (row - 2 > 0) and (column - 2 >= 1) and self.board[row - 2][column - 2] == self.board[row][column]:
                    topL_bottomR += 1
                    if (row - 3 > 0) and (column - 3 >= 1) and self.board[row - 3][column - 3] == self.board[row][column]:
                        topL_bottomR += 1
            if (row + 1 <= 6) and (column + 1 <= 6) and (self.board[row + 1][column + 1] == self.board[row][column]):
                topL_bottomR += 1
                if (row + 2 <= 6) and (column + 2 <= 6) and (self.board[row + 2][column + 2] == self.board[row][column]):
                    topL_bottomR += 1
                    if (row + 3 <= 6) and (column + 3 <= 6) and (self.board[row + 3][column + 3] == self.board[row][column]):
                        topL_bottomR += 1
            if topL_bottomR >= 4:
                return "Winner"
            #check horizontal
            horizontal = 1
            if (column + 1 <= 6) and (self.board[row][column] == self.board[row][column + 1]):
                horizontal += 1
                if (column + 2 <= 6) and (self.board[row][column] == self.board[row][column + 2]):
                    horizontal += 1
                    if (column + 3 <= 6) and (self.board[row][column] == self.board[row][column + 3]):
                        horizontal += 1
            if (column - 1 >= 0) and (self.board[row][column] == self.board[row][column - 1]):
                horizontal += 1
                if (column - 2 >= 0) and (self.board[row][column] == self.board[row][column - 2]):
                    horizontal += 1
                    if (column - 3 >= 0) and (self.board[row][column] == self.board[row][column - 3]):
                        horizontal += 1
            if horizontal >= 4:
                return "Winner"
            return





new_game = Game()
new_game.representation()
game_on = 'continue'
turn = 1
while game_on == 'continue':
    if turn % 2 == 0:
        game_on = new_game.placement(int(input("What row would you like to place your chip in? >> ")), "|X|")
        turn += 1
        continue
    if turn % 2 != 0:
        game_on = new_game.placement(int(input("What row would you like to place your chip in? >> ")), "|O|")
        turn += 1




