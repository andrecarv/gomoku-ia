'''
Created on Sep 5, 2016

@author: andre
'''

class UserInput(object):
    '''
    classdocs
    '''


    def __init__(self, main_window, game):
        '''
        Constructor
        '''
        self.main_window = main_window
        self.game = game
        self.main_window.set_connections(self)
        pass
    
    def square_clicked(self):
        square = self.main_window.sender()
        position = square.get_position()
        if self.game.put_piece_at(position):
            self.main_window.put_piece(position, self.game.active_player_color())
            self.main_window.change_player_turn(self.game.get_active_player())
            
    def new_game(self):
        self.game.new_game()
        self.main_window.clean()
