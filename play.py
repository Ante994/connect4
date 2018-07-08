import os
import time

from connect4 import Connect4
from agent import Agent
from player import Player

if __name__ == '__main__':
    game = Connect4()
    player_one = None
    player_two = None

    os.system('cls')
    print("CONNECT4 GAME:")
    print("\nTko je prvi igrač 'O' ili 'A': (osoba ili agent) ? ")
    while player_one == None:
        input_choice = str(input("Unesi 'O' ili 'A':"))
        if input_choice == 'O' or input_choice == 'A':
            name = str(input("Ime 1. igrača ? "))
            if input_choice == 'A':
                player_one = Agent(name, 'x', difficulty=2)
            else:
                player_one = Player(name, 'x')
        else:
            print("Pogrešan unos, unesite O za odabir korinika ili A za agenta.")
    
    print("\nTko je drugi igrač 'O' ili 'A': (osoba ili agent) ? ")
    while player_two == None:
        input_choice = str(input("Unesi 'O' ili 'A':"))
        if input_choice == 'O' or input_choice == 'A':
            name = str(input("Ime 2. igrača ? "))
            if input_choice == 'A':
                player_two = Agent(name, 'o', difficulty=1)
            else:
                player_two = Player(name, 'o')
        else:
            print("Pogrešan unos, unesite O za odabir korinika ili A za agenta.")


    game.print_board()
    
    while not game.finished or game.round == 42:
        move = 'START'
        if game.get_turn() == 'x':
            print("\nPlayer {0}'s turn!".format(player_one.get_name()))
            if isinstance(player_one, Player):
                while not player_one.legal_move(move, game):
                    move = int(input("Odaberi za potez: (1-7):")) - 1                
            else:
                move = player_one.select_move(game) 
                move = move
            
            if game.make_move(move, player_one.get_color())[1]:
                game.finished_game(player_one)
                game.print_board()
        else:
            print("\nPlayer {0}'s turn!".format(player_two.get_name()))
            if isinstance(player_two, Player):
                while not player_two.legal_move(move, game):
                    move = int(input("Odaberi za potez: (1-7):")) - 1                
            else:
                move = player_two.select_move(game)    
                move = move
            
            
            if game.make_move(move, 'o')[1]:
                time.sleep(0.5)
                game.finished_game(player_two)
                game.print_board()
        
        
    # izmedu korisnika i agenta
    # izmedu agenta i random agenta