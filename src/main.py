'''
Created on Aug 29, 2016

@author: andre
'''
from model.board import Board
from model.piece import Piece
from model.position import Position

if __name__ == '__main__':
    board = Board()
#     [board.insert_piece(Piece(Position(x,0), "black")) for x in range(4)]
    for x in range(5):
        p = Piece(Position(x,0), "black")
        board.insert_piece(p)
    p = board.piece_at((0,0))
    print(board.verify_game_over())
    
#     p1 = Piece(Position(0,0), "black")
#     p2 = Piece(Position(1,0), "black")
#     p3 = Piece(Position(2,0), "black")
#     p4 = Piece(Position(3,0), "black")
#     p5 = Piece(Position(4,0), "black")
    

    pass