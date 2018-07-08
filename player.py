    
class Player:
    
    def __init__(self, name='TESTER', color='x'):
        self.type = "OSOBA"
        self.name = name
        self.color = color

    def legal_move(self, choice, state):
        if choice == 'START':
            return False

        if 0 >= choice > 6:
            print("Pogrešan unos, unijeti 1-7")
            return False
        
        if state.board[5][choice] != ' ':
            print("Ovaj stupac je pun, odaberite drugi")
            return False
        
        
        return True

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color