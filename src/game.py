'''
Created on Sep 5, 2016

@author: andre
'''
from control.user_input import UserInput
from gui.main_window import MainWindow
from gui.dialog_new_game import Ui_DialogNewGame
from model.board import Board
from model.piece import Piece
from PyQt5.QtWidgets import QDialog

PLAYER_COLOR = {1: 'green', -1:'red'}

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

        self.dialog_new_game = QDialog()
        self.ui = Ui_DialogNewGame()
        self.ui.setupUi(self.dialog_new_game)

        self.user_input = UserInput(main_window, self)
        self.new_game()
        self.over = False
        main_window.show()
        
    def new_game(self):
        self.dialog_new_game.exec()
        print(self.ui.is_player2_human)
        print(self.ui.difficulty)

        self.board = Board()
        self.over = False
        self.active_player = 1
        
    def put_piece_at(self, position):
        if self.board.put_piece(Piece(position, PLAYER_COLOR[self.active_player])):
            self.active_player = -self.active_player
            return True
        return False
    
    def check_game_end(self):
        result = self.board.verify_game_over()
        if result == 'end':
            self.over = True
        return result
    
    def active_player_color(self):
        return PLAYER_COLOR[self.active_player]
        
    def get_active_player(self):
        return self.active_player
    
    def is_over(self):
        return self.over
