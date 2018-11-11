
from random import choice

class Agent:
    ROWS = 6
    COLUMNS = 7

    def __init__(self, name='BOT', color='o', difficulty=1):
        self.type = "AI"
        self.name = name
        self.color = color
        self.difficulty = difficulty
        self.node_cnt = 0
    
    def select_move(self, state):
        if self.difficulty == 2:
            return self.best_move(state)
        else:
            return choice(state.all_moves())[1]

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color

    def best_move(self, state):
        self.node_cnt = 0
        #val, move = self.minimax(state, 2)
        val, move = self.alphabeta(state, -99999, 99999, 2)
        print('Value:', val, 'Move:', move + 1, 'Nodes:', self.node_cnt)
        return move

    def evaluate(self, state):
        my_streakTEST = 0

        streak_vertical = self.vertical_streak(state.board, 'x')
        streak_horizontal = self.horizontal_streak(state.board, 'x')
        streak_diagonal = self.diagonal_streak(state.board, 'x')

        if state.board[0][3] == 'x':
            my_streakTEST += 5
        elif state.board[0][3] == 'o':
            my_streakTEST -= 5

        for streak in streak_vertical, streak_horizontal, streak_diagonal:
            if streak == 4:
                my_streakTEST +=  streak * 1000
            elif streak == 3:
                my_streakTEST += streak * 100
            elif streak == 2:
                my_streakTEST += streak * 10
            
        opp_streak_vertical = self.vertical_streak(state.board, 'o')
        opp_streak_horizontal = self.horizontal_streak(state.board, 'o')
        opp_streak_diagonal = self.diagonal_streak(state.board, 'o')
        opp_streak = max(opp_streak_vertical, opp_streak_horizontal, opp_streak_diagonal)
                
		if opp_streak == 4:
            return -50000
        elif opp_streak == 3 and my_streakTEST < (opp_streak * 100):
            return (opp_streak * -100)
        else:
            return my_streakTEST


    def minimax(self, state, depth):
        self.node_cnt += 1

        if depth == 0 or state.check_for_winning_move():
            #print(state.board, state.all_moves())
            #print("EVAL:", self.evaluate(state))
            return (self.evaluate(state), None)        

        best_val = -9999 if state.turn == 'x' else 9999
        best_move = None
        
        #print(state.board, state.all_moves())

        for m in state.all_moves():
            a = state.make_move(m[1], state.turn)
            
            val, _ = self.minimax(state, depth-1)
            
            state.undo(a, m[1])
            if state.turn == 'x': # max
                if val > best_val:
                    best_val = val
                    best_move = m[1]
            else: # min
                if val < best_val:
                    best_val = val
                    best_move = m[1]

        return (best_val, best_move)

    def alphabeta(self, state, alpha, beta, depth):
        self.node_cnt += 1

        if depth == 0 or state.check_for_winning_move():
            #print(state.board, state.all_moves())
            #print(state.print_board())
            #print("EVAL:", self.evaluate(state))
            return (self.evaluate(state), None)        
        
        best_move = None
        for m in state.all_moves():
            a = state.make_move(m[1], state.turn)
            val, _ = self.alphabeta(state, alpha, beta, depth-1)
            state.undo(a, m[1])
            if state.turn == 'x': # max
                if val > alpha:
                    alpha = val
                    best_move = m[1]
            else: # min
                if val < beta:
                    beta = val
                    best_move = m[1]
            if alpha >= beta: # beta cut
                break
        
        if state.turn == 'x': # max
            return (alpha, best_move)
        else:
            return (beta, best_move)

    def vertical_streak(self, state, color):
        count = 0
        temp = 0

        for c in range(self.COLUMNS):
            for r in range(self.ROWS - 3):
                if color == state[r][c] and state[r][c] == state[r+1][c] and state[r+1][c] == state[r+2][c] and state[r+2][c] == state[r+3][c]:
                    temp = 4
                elif color == state[r][c] and state[r][c] == state[r+1][c] and state[r+1][c] == state[r+2][c] and state[r+3][c] == ' ':
                    temp = 3
                elif color == state[r][c] and state[r][c] == state[r+1][c] and state[r+2][c] ==  ' ' and state[r+3][c] ==  ' ':
                    temp = 2
                if temp > count:
                    count = temp
                    temp = 0
        return count

    def horizontal_streak(self, state, color):
        count = 0
        temp = 0

        for c in range(self.COLUMNS - 3):
            for r in range(self.ROWS):
                if color == state[r][c] and state[r][c] == state[r][c+1] and state[r][c+1] == state[r][c+2] and state[r][c+2] == state[r][c+3]:
                    temp = 4
                elif color == state[r][c] and state[r][c] == state[r][c+1] and state[r][c+1] == state[r][c+2] and state[r][c+3] == ' ':
                    temp = 3
                elif color == state[r][c] and state[r][c] == state[r][c+1] and state[r][c+2] == ' ' and state[r][c+3] == ' ':
                    temp = 2                
                if temp > count:
                    count = temp
                    temp = 0
        return count
    
    def diagonal_streak(self, state, color):
        count = 0
        temp = 0
        count1 = 0
        count2 = 0

        for c in range(self.COLUMNS - 3):
            for r in range(self.ROWS - 3):
                if color == state[r][c] and state[r][c] == state[r+1][c+1] and state[r+1][c+1] == state[r+2][c+2] and state[r+2][c+2] == state[r+3][c+3]:
                    temp = 4
                elif color == state[r][c] and state[r][c] == state[r+1][c+1] and state[r+1][c+1] == state[r+2][c+2] and state[r+3][c+3] == ' ':
                    temp = 3
                elif color == state[r][c] and state[r][c] == state[r+1][c+1] and state[r+2][c+2] == ' ' and state[r+3][c+3] == ' ':
                    temp = 2
                
                if temp > count1:
                    count1 = temp
                    temp = 0

        temp = 0
        
        for c in range(self.COLUMNS - 3):
            for r in range(3, self.ROWS):
                if color == state[r][c] and state[r][c] == state[r-1][c-1] and state[r-1][c-1] == state[r-2][c-2] and state[r-2][c-2] == state[r-3][c-3]:
                    temp = 4
                elif color == state[r][c] and state[r][c] == state[r-1][c-1] and state[r-1][c-1] == state[r-2][c-2] and state[r-3][c-3] == ' ':
                    temp = 3
                elif color == state[r][c] and state[r][c] == state[r-1][c-1] and state[r-2][c-2] == ' ' and state[r-3][c-3] == ' ':
                    temp = 2
                
                if temp > count2:
                    count2 = temp
                    temp = 0

        count = count1 if count1 >= count2 else count2
        return count
