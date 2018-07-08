
class Connect4:
    ROWS = 6
    COLUMNS = 7
    
    def __init__(self, turn='x'):
        self.board = []
        self.turn = turn
        self.winner = None
        self.finished = False
        self.round = 1

        self.create_board()
    
    def get_turn(self):
        return self.turn

    def create_board(self):
        for i in range(self.ROWS):
            self.board.append([])
            for j in range(self.COLUMNS):
                self.board[i].append(' ')

    def all_moves(self):
        moves = []
        
        for column in range(self.COLUMNS):
            for row in range(self.ROWS):
                if self.board[row][column] == ' ':
                    moves.append([row, column])
                    column = 0
                    break
                else:
                    if row < 5:
                        row += 1
                    
        return moves

    def check_vertical(self):
        for c in range(self.COLUMNS):
            for r in range(self.ROWS-3):
                if self.board[r][c] != ' ' and self.board[r][c] == self.board[r+1][c] and self.board[r+1][c] == self.board[r+2][c] and self.board[r+2][c] == self.board[r+3][c]:
                    return True

        return False

    def check_horizontal(self):
        for c in range(self.COLUMNS-3):
            for r in range(self.ROWS):
                if self.board[r][c] != ' ' and self.board[r][c] == self.board[r][c+1] and self.board[r][c+1] == self.board[r][c+2] and self.board[r][c+2] == self.board[r][c+3]:
                    return True
        
        return False

    def check_diagonal(self):
        for c in range(self.COLUMNS-3):
            for r in range(self.ROWS-3):
                if self.board[r][c] != ' ' and self.board[r][c] == self.board[r+1][c+1] and self.board[r+1][c+1] == self.board[r+2][c+2] and self.board[r+2][c+2] == self.board[r+3][c+3]:
                    return True

        for c in range(self.COLUMNS - 3):
            for r in range(3, self.ROWS):
                if self.board[r][c] != ' ' and self.board[r][c] == self.board[r-1][c+1] and self.board[r-1][c+1] == self.board[r-2][c+2] and self.board[r-2][c+2] == self.board[r-3][c+3]:
                    return True
        
        return False

    def check_for_winning_move(self):
        if self.check_horizontal() or self.check_vertical() or self.check_diagonal():
            return True

    def finished_game(self, player):
        if self.check_horizontal() or self.check_vertical() or self.check_diagonal():
            #print("\nGame over! Player {0} WIN!". format(player.get_name()))
            self.finished = True
            self.winner = player

    def make_move(self, choice, player):
        val, valid = self.is_valid_move(choice, player)
        if valid:
            self.board[val][choice] = player
            self.round += 1
            self.turn = 'x' if self.turn == 'o' else 'o'
            self.undo_row = val
            return val, True
        
        return False

    def undo(self, row, choice):
        self.board[row[0]][choice] = ' '
        self.turn = 'x' if self.turn == 'o' else 'o'
        self.finished = False
        self.round -= 1

    def is_valid_move(self, choice, player):
        for i in range(6):
            if self.board[i][choice] == ' ':
                return i, True
        
        print("This Column is Full!")
        
        return False

    def print_board(self):
        print("Round: " + str(self.round))

        for i in range(5, -1, -1):
            print("\t", end="")
            for j in range(7):
                print("| " + str(self.board[i][j]), end=" ")
            print("|")
        print("\t  _   _   _   _   _   _   _ ")
        print("\t  1   2   3   4   5   6   7 ")
    