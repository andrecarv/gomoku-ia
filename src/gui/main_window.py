'''
Created on Sep 5, 2016

@author: andre
'''
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QGridLayout,\
    QHBoxLayout, QDialog
from PyQt5.QtGui import QFont
from model.position import Position
from PyQt5.Qt import QWidget, QPushButton


class MainWindow(QMainWindow):
    
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setWindowTitle("Gomoku")
        self.player1 = True
        self.p1_txt = "Player 1 ( x )"
        self.p2_txt = "Player 2 ( o )"
        self.resize(800, 600)  # 493, 478
        
        self.initUI()
        
    def initUI(self):
        self.centralw = QWidget()
        
        self.v_layout = QVBoxLayout(self.centralw)
        self.v_layout.setContentsMargins(11, 11, 11, 11)
        self.v_layout.setSpacing(6)
        
        hlayout = QHBoxLayout()
        hlayout.setContentsMargins(11, 11, 11, 11)
        hlayout.setSpacing(0)
        self.v_layout.addLayout(hlayout)
        
        self.new_game_btn = QPushButton("New Game")
        self.new_game_btn.setFixedSize(self.new_game_btn.sizeHint())
        self.new_game_btn.clicked.connect(self.new_game)
        hlayout.addWidget(self.new_game_btn)
        
        ###
        def end_game_dialog():
            d = QDialog()
            lay = QHBoxLayout()
            lbl = QLabel("Player x won")
            lay.addWidget(lbl)
            d.setLayout(lay)
            d.exec_()
        end_game = QPushButton("End Game")
        hlayout.addWidget(end_game)
        end_game.clicked.connect(end_game_dialog)
        ###
        
        hlayout.addStretch(1)
        
        self.player_turn = QLabel("Player Turn: ")
        self.player_turn.setFixedSize(self.player_turn.sizeHint())
        self.player_lbl = QLabel(self.p1_txt)
        self.player_lbl.setFixedSize(self.player_lbl.sizeHint())
        hlayout.addWidget(self.player_turn)
        hlayout.addWidget(self.player_lbl)
    
        
        self.board_layout = QGridLayout()
        self.board_layout.setContentsMargins(11, 11, 11, 11)
        self.board_layout.setSpacing(0)
        
        self.v_layout.addLayout(self.board_layout)
        
        self.setCentralWidget(self.centralw)
        
        # QMetaObject.connectSlotsByName(MainWindow)
        
        for i in range(15):
            for j in range(15):
                sq = Square(Position(i, j))
                self.board_layout.addWidget(sq, i, j)
                sq.clicked.connect(self.square_clicked)
                
    def square_clicked(self):
        square = self.sender()
        print(square.get_position())
        if square.text() is "":
            if self.player1 == True:
                square.setText("x")
                self.player_lbl.setText(self.p2_txt)
            else:
                square.setText("o")
                self.player_lbl.setText(self.p1_txt)
            self.player1 = not self.player1
    
    def new_game(self):
        pass
    
class Square(QLabel):
    clicked = pyqtSignal()
    
    def __init__(self, position):
        super(QLabel, self).__init__()
        self.position = position
        self.initUI()
        
    def initUI(self):
        self.setStyleSheet("QLabel { background-color: white; border-style: outset; border-width: 1px;border-color: black; }")
        self.setAlignment(Qt.AlignCenter)
        self.setFont(QFont("MS Shell Dlg 2", 14, QFont.Bold))
        
    def get_position(self):
        return self.position
    
    def mousePressEvent(self, event):
        self.clicked.emit()
