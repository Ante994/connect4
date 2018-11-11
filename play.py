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
    print("\nWho playing first ? 'P' ili 'A': (person or agent) ? ")
    while player_one == None:
        input_choice = str(input("Choose 'P' ili 'A':"))
        if input_choice == 'P' or input_choice == 'A':
            name = str(input("Name for first player ? "))
            if input_choice == 'A':
                player_one = Agent(name, 'x', difficulty=2)
            else:
                player_one = Player(name, 'x')
        else:
            print("Wrong input, choose P for person playing or A for agent.")
    
	print("\nWho playing second ? 'P' ili 'A': (person or agent) ? ")
    while player_two == None:
        input_choice = str(input("Choose 'P' ili 'A':"))
        if input_choice == 'P' or input_choice == 'A':
            name = str(input("Name for second player ? "))
            if input_choice == 'A':
                player_two = Agent(name, 'o', difficulty=1)
            else:
                player_two = Player(name, 'o')
        else:
            print("Wrong input, choose P for person playing or A for agent.")


    game.print_board()
    
    while not game.finished or game.round == 42:
        move = 'START'
        if game.get_turn() == 'x':
            print("\nPlayer {0}'s turn!".format(player_one.get_name()))
            if isinstance(player_one, Player):
                while not player_one.legal_move(move, game):
                    move = int(input("Choose move: (1-7):")) - 1                
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
                    move = int(input("Choose move: (1-7):")) - 1                
            else:
                move = player_two.select_move(game)    
                move = move
            
            
            if game.make_move(move, 'o')[1]:
                time.sleep(0.5)
                game.finished_game(player_two)
                game.print_board()
        
        
