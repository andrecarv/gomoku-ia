'''
Created on Sep 5, 2016

@author: andre
'''
from PyQt5.Qt import QWidget, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QPixmap, QImage, QPalette
from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QGridLayout, \
    QHBoxLayout, QDialog

from model.position import Position


COLOR_URL = {'black' : 'black.png', 'white':'white.png'}
PLAYERS = {1:'Player 1 (green)', -1:'Player 2 (red)'}

class MainWindow(QMainWindow):
    
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setWindowTitle("Gomoku")
        self.resize(800, 600)  # 493, 478
        self.squares = []
        
        self.initUI()
        
    def initUI(self):
        self.central_widget = QWidget()
        
        self.v_layout = QVBoxLayout(self.central_widget)
        self.v_layout.setContentsMargins(11, 11, 11, 11)
        self.v_layout.setSpacing(6)
        
        hlayout = QHBoxLayout()
        hlayout.setContentsMargins(11, 11, 11, 11)
        hlayout.setSpacing(0)
        self.v_layout.addLayout(hlayout)
        
        self.new_game_btn = QPushButton("New Game")
        self.new_game_btn.setFixedSize(self.new_game_btn.sizeHint())
        hlayout.addWidget(self.new_game_btn)
        
        hlayout.addStretch(1)
        
        player_lbl = QLabel("Player Turn: ")
        player_lbl.setFixedSize(player_lbl.sizeHint())
        self.active_player_lbl = QLabel(PLAYERS[1])
        self.active_player_lbl.setFixedSize(self.active_player_lbl.sizeHint())
        hlayout.addWidget(player_lbl)
        hlayout.addWidget(self.active_player_lbl)
    
        
        self.board_layout = QGridLayout()
        self.board_layout.setContentsMargins(11, 11, 11, 11)
        self.board_layout.setSpacing(0)
        
        self.v_layout.addLayout(self.board_layout)
        
        self.setCentralWidget(self.central_widget)
        
        for i in range(15):
            for j in range(15):
                sq = Square(Position(i, j))
                self.squares.append(sq)
                self.board_layout.addWidget(sq, i, j)
                
    def put_piece(self, position, color):
        label = self.sender()
#         image = QImage()
#         image.load(COLOR_URL[color])
#         label.setPixmap(QPixmap.fromImage(image))
        label.setStyleSheet("QLabel { background-color: %s; border-style: outset; border-width: 1px;border-color: black;}" % color)
        label.show()
#         label.setText("X")
#         label.setPixmap(QPixmap(COLOR_URL[color]))
        
    def change_player_turn(self, active_player):
        self.active_player_lbl.setText(PLAYERS[active_player])
    
    def clean(self):
        self.active_player_lbl.setText(PLAYERS[1])
        for square in self.squares:
            square.initUI()
            
    def four_sequence_warning(self):
        d = QDialog()
        hlayout = QHBoxLayout()
        lbl = QLabel("You're loosing Idiot!")
        hlayout.addWidget(lbl)
        d.setLayout(hlayout)
        d.exec_()
            
    def game_over(self):
        d = QDialog()
        hlayout = QHBoxLayout()
        lbl = QLabel("The winner is %s" % self.active_player_lbl.text())
        hlayout.addWidget(lbl)
        d.setLayout(hlayout)
        d.exec_()
    
    def set_connections(self, user_input):
        for square in self.squares:
            square.clicked.connect(user_input.square_clicked)
        self.new_game_btn.clicked.connect(user_input.new_game)
    
class Square(QLabel):
    clicked = pyqtSignal()
    
    def __init__(self, position):
        super(QLabel, self).__init__()
        self.position = position
        self.setScaledContents(True)
        self.initUI()
        
    def initUI(self):
        self.setStyleSheet("QLabel { background-color: white; border-style: outset; border-width: 1px;border-color: black; }")
        self.setAlignment(Qt.AlignCenter)
        self.setFont(QFont("MS Shell Dlg 2", 14, QFont.Bold))
#         self.setPixmap(None)
        
    def get_position(self):
        return self.position
    
    def mousePressEvent(self, event):
        self.clicked.emit()
