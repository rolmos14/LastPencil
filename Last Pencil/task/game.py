class Game:

    def run(self):
        pass


class PenPaperGame(Game):

    valid_picks = ['1', '2', '3']

    def __init__(self):
        self.pens = 0
        self.users = ["Tik", "Tok"]
        self.turn = 0

    def get_initial_pens(self):
        print("How many pencils would you like to use:")
        while True:
            ini_pens = input()
            if self.valid_initial_pens(ini_pens):
                self.pens = int(ini_pens)
                break

    def valid_initial_pens(self, pens):
        if not pens.isnumeric() or int(pens) < 0:
            print("The number of pencils should be numeric")
            return False
        elif pens == '0':
            print("The number of pencils should be positive")
            return False
        return True

    def pick_pens(self):
        while True:
            picked_pens = input()
            if picked_pens not in self.valid_picks:
                print(f"Possible values: "
                      f"'{self.valid_picks[0]}', '{self.valid_picks[1]}' or '{self.valid_picks[2]}'")
            elif int(picked_pens) > self.pens:
                print("Too many pencils were taken")
            else:
                self.pens -= int(picked_pens)
                break

    def game_over(self):
        return self.pens == 0

    def show_winner(self):
        print(f"{self.users[self.turn]} won!")

    def get_initial_player(self):
        print(f"Who will be the first ({self.users[0]}, {self.users[1]}):")
        while True:
            first_turn = input()
            try:
                self.turn = self.users.index(first_turn)
                break
            except ValueError:
                print(f"Choose between '{self.users[0]}' and '{self.users[1]}'")

    def change_user(self):
        self.turn = 1 if self.turn == 0 else 0

    def __str__(self):
        return self.pens * "|" + f"\n{self.users[self.turn]}'s turn:"

    def run(self):
        self.get_initial_pens()
        self.get_initial_player()
        while not self.game_over():
            print(self)
            self.pick_pens()
            self.change_user()
        self.show_winner()


pen_paper = PenPaperGame()
pen_paper.run()
