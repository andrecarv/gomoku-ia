'''
Created on Aug 29, 2016

@author: andre
'''
from PyQt5.QtWidgets import QApplication
import sys

from game import Game

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = Game()
    sys.exit(app.exec_())
    
