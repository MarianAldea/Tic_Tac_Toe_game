class CheckWinner():
    def __init__(self):
        self.win_conditions = [[0, 1 , 2], [3, 4, 5], [6, 7 ,8], [0, 4, 8], [2, 4, 6], [0, 3 ,6], [1, 4 ,7], [1, 5 ,8]]
        self.game_on = True
        self.winner = ""

    def verify_winner(self, turn_number, letter, checked_boxes):
        list = [i for i, x in enumerate(checked_boxes) if x == letter]
        if list in self.win_conditions:
            self.winner = letter
            self.game_on = False

        if turn_number == 9 and self.game_on:
            self.winner = "DRAW"
            self.game_on = False
        if self.winner == "DRAW" and not self.game_on:
            print("It's a DRAW")
        elif self.winner == "X" and not self.game_on:
            print("X won the game")
        elif self.winner == "0" and not self.game_on:
            print("0 won the game")

    def restart_game(self):
        self.game_on = True
        print(self.game_on)
