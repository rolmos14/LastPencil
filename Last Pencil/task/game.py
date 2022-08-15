class Game:

    def run(self):
        pass


class PenPaperGame(Game):

    def __init__(self):
        self.pens = 0
        self.users = ["Tik", "Tok"]
        self.turn = 0

    def run(self):
        print("How many pencils would you like to use:")
        self.pens = int(input())
        print(f"Who will be the first ({self.users[0]}, {self.users[1]}):")
        first_turn = input()
        self.turn = self.users.index(first_turn)
        while self.pens > 0:
            print(self.pens * "|")
            print(f"{self.users[self.turn]}'s turn:")
            picked_pens = int(input())
            self.pens -= picked_pens
            self.turn = 1 if self.turn == 0 else 0


pen_paper = PenPaperGame()
pen_paper.run()
