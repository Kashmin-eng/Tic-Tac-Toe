import math
import random
from typing import Sequence

class Player:
    def __init__(self, letter):
        #letter is x or o
        self.letter = letter

        #we want all player to get thir next move
        def get_move(self, game):
            pass

class RamdoomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # get a random valid spot for out next move
        square = random.choice(game.available_move())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            Square = input (self.letter + '\'s turn. Input move (0-9:)')
            # we're goint to check that this is a correct value by trying to cast
            #it to an integer, and if it's not, then we say its invalid
            #if that sopt is not availablee on the board, we also say its invalid
            try:
                val =int(Square)
                if val not in game.available_move:
                    raise ValueError
                valid_square = True # If these are successful, then good !!
            except ValueError:
                print ('Invalid Square. Try again')
        
        return val
                 
