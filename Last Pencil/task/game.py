class Game:

    def run(self):
        pass


class PenPaperGame(Game):

    def __init__(self):
        self.pens = 4
        self.turn = "User"

    def run(self):
        print(self.pens * "|")
        if self.turn == "User":
            print("Your turn!")
        else:
            print("Computer's turn")


pen_paper = PenPaperGame()
pen_paper.run()
