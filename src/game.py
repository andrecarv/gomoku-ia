'''
Created on Sep 5, 2016

@author: andre
'''
from control.user_input import UserInput
from gui.main_window import MainWindow
from model.board import Board
from model.piece import Piece
PLAYER_COLOR = {1: 'black', -1:'white'}

class Game(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.board = None
        main_window = MainWindow()
        self.user_input = UserInput(main_window, self)
        self.new_game()
        main_window.show()
        
    def new_game(self):
        self.board = Board()
        self.active_player = 1
        
    def put_piece_at(self, position):
        if self.board.put_piece(Piece(position, PLAYER_COLOR[self.active_player])):
            self.active_player = -self.active_player
            return True
        return False
        
    def active_player_color(self):
        return PLAYER_COLOR[self.active_player]
        
    def get_active_player(self):
        return self.active_player
