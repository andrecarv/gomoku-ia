# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_new_game.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

#from PyQt5.Qt import QWidget, QPushButton
#from PyQt5.QtCore import Qt, pyqtSignal
##from PyQt5 import QtCore, QtGui, QtWidgets
#import sys
#from PyQt5.QtCore import Qt
#from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, 
#    QVBoxLayout, QApplication)

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogNewGame(object):
    
    def setReturnValues(self):
        self.is_player2_human = self.radio_button_human.isChecked()
        if self.radio_button_easy.isChecked():
            self.difficulty = 2
        if self.radio_button_medium.isChecked():
            self.difficulty = 3
        if self.radio_button_hard.isChecked():
            self.difficulty = 4
        self.dialog.accept()
        
    def setupUi(self, DialogNewGame):
        self.dialog = DialogNewGame
        self.dialog.setObjectName("DialogNewGame")
        self.dialog.resize(200, 280)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dialog.sizePolicy().hasHeightForWidth())
        self.dialog.setSizePolicy(sizePolicy)
        self.dialog.setMinimumSize(QtCore.QSize(200, 280))
        self.dialog.setMaximumSize(QtCore.QSize(200, 280))
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.dialog)
        self.verticalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_player = QtWidgets.QFrame(self.dialog)
        self.frame_player.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_player.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_player.setLineWidth(1)
        self.frame_player.setObjectName("frame_player")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_player)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame_player)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.radio_button_human = QtWidgets.QRadioButton(self.frame_player)
        self.radio_button_human.setChecked(True)
        self.radio_button_human.setObjectName("radio_button_human")
        self.verticalLayout.addWidget(self.radio_button_human)
        self.radio_button_computer = QtWidgets.QRadioButton(self.frame_player)
        self.radio_button_computer.setObjectName("radio_button_computer")
        self.verticalLayout.addWidget(self.radio_button_computer)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_5.addWidget(self.frame_player)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.frame_difficulty = QtWidgets.QFrame(DialogNewGame)
        self.frame_difficulty.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_difficulty.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_difficulty.setObjectName("frame_difficulty")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_difficulty)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_difficulty)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.radio_button_easy = QtWidgets.QRadioButton(self.frame_difficulty)
        self.radio_button_easy.setChecked(True)
        self.radio_button_easy.setObjectName("radio_button_easy")
        self.verticalLayout_2.addWidget(self.radio_button_easy)
        self.radio_button_medium = QtWidgets.QRadioButton(self.frame_difficulty)
        self.radio_button_medium.setObjectName("radio_button_medium")
        self.verticalLayout_2.addWidget(self.radio_button_medium)
        self.radio_button_hard = QtWidgets.QRadioButton(self.frame_difficulty)
        self.radio_button_hard.setObjectName("radio_button_hard")
        self.verticalLayout_2.addWidget(self.radio_button_hard)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_5.addWidget(self.frame_difficulty)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.button_ok = QtWidgets.QPushButton(self.dialog)
        self.button_ok.setObjectName("button_ok")
        self.horizontalLayout.addWidget(self.button_ok)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.retranslateUi(self.dialog)
        QtCore.QMetaObject.connectSlotsByName(self.dialog)

        self.button_ok.clicked.connect(self.setReturnValues)

    def retranslateUi(self, DialogNewGame):
        _translate = QtCore.QCoreApplication.translate
        self.dialog.setWindowTitle(_translate("DialogNewGame", "New Game"))
        self.label.setText(_translate("DialogNewGame", "Play with player 2:"))
        self.radio_button_human.setText(_translate("DialogNewGame", "Human"))
        self.radio_button_computer.setText(_translate("DialogNewGame", "Computer"))
        self.label_2.setText(_translate("DialogNewGame", "Dificulty"))
        self.radio_button_easy.setText(_translate("DialogNewGame", "Easy"))
        self.radio_button_medium.setText(_translate("DialogNewGame", "Medium"))
        self.radio_button_hard.setText(_translate("DialogNewGame", "Hard"))
        self.button_ok.setText(_translate("DialogNewGame", "Ok"))

