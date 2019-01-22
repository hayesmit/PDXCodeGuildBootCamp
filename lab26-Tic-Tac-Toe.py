# lab26-Tic-Tac-Toe.py
#create a new game with an empty game board as well in order to later check to make sure players arent trying to go into occupied locations
class Game:
    def __init__(self):
        self.board = ["|1|", "|2|", "|3|", "|4|", "|5|", "|6|", "|7|", "|8|", "|9|"]
        self.empty_board = ['', '', '', '', '', '', '', '', '']

    def board_representation(self):
        representation = []
        for i in range(0, 9, 3):
            representation.append(self.board[i])
            representation.append(self.board[i + 1])
            representation.append(self.board[i + 2])
            representation.append('\n')
        print(''.join(representation))

    def __repr__(self):
        return str(self.board)

# changes the gameboard and empty game board to reflect user choice and
    def move(self, selection, player):
        global counter
        if self.empty_board[selection-1] == '':
            self.board[selection - 1] = player
            self.empty_board[selection - 1] = player
            self.check_for_winner()
        else:
            print('sorry at placement is already taken')
            self.move(int(input("where would you like to go? >>")), player)

    def check_for_winner(self):
        print(self.board_representation())
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6]:
                print('winner winnner winner')
                return False
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i + 1] == self.board[i + 2]:
                print('Winner winner winner')
                return False
        if (self.board[0] == self.board[4] == self.board[8]) or self.board[2] == self.board[4] == self.board[6]:
            print("Winner winner winner")
            return False
        return True


start_game = Game()
counter = 0
while start_game.check_for_winner():
    player1 = '|X|'
    player2 = '|O|'
    if counter % 2 == 0:
        start_game.move(int(input("select your position >> ")), player1)
        counter += 1
        if (counter == 9) and start_game.check_for_winner():
            print('cats game, you both must be very good at this game')
            break
    elif counter % 2 != 0:
        start_game.move(int(input("select your position >> ")), player2)
        counter += 1


