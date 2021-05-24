from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
import sys


class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        """
        This initializes all the windows properties and window objects like label and buttons
        :return:
        """

        # Window properties
        self.setWindowTitle("TicTacToe ")
        self.resize(370, 461)

        # Title label
        self.label = QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 20, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Handwriting")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText("Tic Tac Toe")

        # Player 1 score label
        self.player1_score = QLabel(self)
        self.player1_score.setGeometry(QtCore.QRect(20, 70, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        self.player1_score.setFont(font)

        # Player 2 score label
        self.player2_score = QLabel(self)
        self.player2_score.setGeometry(QtCore.QRect(220, 70, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        self.player2_score.setFont(font)
        self.player2_score.setAlignment(QtCore.Qt.AlignCenter)

        # Board button[1]
        self.b1 = QPushButton(self)
        self.b1.setGeometry(QtCore.QRect(10, 100, 111, 111))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.b1.setFont(font)

        # Board button[2]
        self.b2 = QPushButton(self)
        self.b2.setGeometry(QtCore.QRect(130, 100, 111, 111))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.b2.setFont(font)

        # Board button[3]
        self.b3 = QPushButton(self)
        self.b3.setGeometry(QtCore.QRect(250, 100, 111, 111))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.b3.setFont(font)

        # Board button[4]
        self.b4 = QPushButton(self)
        self.b4.setGeometry(QtCore.QRect(10, 220, 111, 111))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.b4.setFont(font)

        # Board button[5]
        self.b5 = QPushButton(self)
        self.b5.setGeometry(QtCore.QRect(130, 220, 111, 111))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.b5.setFont(font)

        # Board button[5]
        self.b6 = QPushButton(self)
        self.b6.setGeometry(QtCore.QRect(250, 220, 111, 111))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.b6.setFont(font)

        # Board button[7]
        self.b7 = QPushButton(self)
        self.b7.setGeometry(QtCore.QRect(10, 340, 111, 111))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.b7.setFont(font)

        # Board button[8]
        self.b8 = QPushButton(self)
        self.b8.setGeometry(QtCore.QRect(130, 340, 111, 111))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.b8.setFont(font)

        # Board button[9]
        self.b9 = QPushButton(self)
        self.b9.setGeometry(QtCore.QRect(250, 340, 111, 111))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.b9.setFont(font)

    def reset_buttons(self):
        """
        Resets board buttons
        """
        self.b9.setText(" ")
        self.b9.setEnabled(True)
        self.b8.setText(" ")
        self.b8.setEnabled(True)
        self.b7.setText(" ")
        self.b7.setEnabled(True)
        self.b6.setText(" ")
        self.b6.setEnabled(True)
        self.b5.setText(" ")
        self.b5.setEnabled(True)
        self.b4.setText(" ")
        self.b4.setEnabled(True)
        self.b3.setText(" ")
        self.b3.setEnabled(True)
        self.b2.setText(" ")
        self.b2.setEnabled(True)
        self.b1.setText(" ")
        self.b1.setEnabled(True)

    def reset_labels(self):
        """
        Resets scores of each player
        """
        self.player2_score.setText("Player 2: 0")
        self.player1_score.setText("Player 1: 0")

    def reset_components(self):
        """
        Resets labels and buttons
        """
        self.reset_labels()
        self.reset_buttons()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppWindow()
    sys.exit(app.exec())
