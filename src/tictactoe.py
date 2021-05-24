from PyQt5.QtWidgets import *
from gui import AppWindow

class Game(AppWindow):

    def __init__(self):

        super().__init__()
        self.set_comp()

        #Add action to clickable buttons
        self.b1.clicked.connect(self.action)
        self.b2.clicked.connect(self.action)
        self.b3.clicked.connect(self.action)
        self.b4.clicked.connect(self.action)
        self.b5.clicked.connect(self.action)
        self.b6.clicked.connect(self.action)
        self.b7.clicked.connect(self.action)
        self.b8.clicked.connect(self.action)
        self.b9.clicked.connect(self.action)

    def set_comp(self):
        """
        This will initialize the labels, buttons of the app and  flags required
        """
        self.reset_components()
        self.turn = 1
        self.count = 0
        self.p1_score = 0
        self.p2_score = 0
        self.player_won = 0

    def reset_comp(self):
        """
        This will reset the buttons and flags required but not the scores of the players
        """
        self.reset_buttons()
        self.turn = 2
        self.count = 0
        self.player_won = 0

    def action(self):
        """
        This will be called when a board button is clicked.
        """
        button = self.sender()
        self.count += 1
        if self.turn == 1:
            button.setText("X")
            button.setEnabled(False)

        else:
            button.setText("O")
        button.setEnabled(False)

        if self.count >= 5 :
            self.player_won = self.check_win()
            if self.player_won != 0:
                self.game_msg()
            if self.count == 9:
                self.game_msg()
        self.turn = 2 if self.turn == 1 else 1

    def check_win(self):
        """
        Checks if theres three of the same player in rows or cols
        top row: 1 = 2 = 3    middle row: 4 = 5 = 6     bottom row: 7 = 8 = 9
        left col: 1 = 4 = 7   middle col: 2 = 5 = 8     right col: 3 = 6 = 9
        diagonal: 1 = 5 = 7 or 3 = 5 = 7
        :return player number if a player wins else returns 0
        """

        top_row = (self.b1.text() == self.b2.text() == self.b3.text() != " ")
        middle_row = (self.b4.text() == self.b5.text() == self.b6.text() != " ")
        bottom_row = (self.b7.text() == self.b8.text() == self.b9.text() != " ")

        left_col = (self.b1.text() == self.b4.text() == self.b7.text() != " ")
        middle_col = (self.b2.text() == self.b5.text() == self.b8.text() != " ")
        right_col = (self.b3.text() == self.b6.text() == self.b9.text() != " ")

        diagonal1 = (self.b1.text() == self.b5.text() == self.b9.text() != " ")
        diagonal2 = (self.b3.text() == self.b5.text() == self.b7.text() != " ")

        if top_row or middle_row or bottom_row or left_col or middle_col or right_col or diagonal1 or diagonal2:
            return self.turn

        return 0

    def game_msg(self):
        """
        This will give a pop message for the winning player and will ask whether the player wants to play again.
        """
        msg = QMessageBox()
        if self.player_won != 0:
            msg.setWindowTitle("Player {} Wins!".format(self.player_won))
            if self.player_won == 1:
                self.p1_score += 1
                self.player1_score.setText("Player 1: {}".format(self.p1_score))
            else:
                self.p2_score += 1
                self.player2_score.setText("Player 2: {}".format(self.p2_score))
        else:
            msg.setWindowTitle("Its a Tie!")
        msg.setText("Do you want to play again?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        response = msg.exec_()
        if response == QMessageBox.Yes:
            self.reset_comp()
        else:
            self.set_comp()


def main():
    """Main function of the game"""
    app = QApplication([])
    new_game = Game()
    app.exec_()


if __name__ == "__main__":
    main()