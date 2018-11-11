    
class Player:
    
    def __init__(self, name='TESTGUY', color='x'):
        self.type = "PERSON"
        self.name = name
        self.color = color

    def legal_move(self, choice, state):
        if choice == 'START':
            return False

        if 0 >= choice > 6:
            print("Wrong input, choose from 1 to 7")
            return False
        
        if state.board[5][choice] != ' ':
            print("Column is full")
            return False
        
        
        return True

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color