class Game:

    def run(self):
        pass


class PenPaperGame(Game):

    def __init__(self):
        self.pens = 0
        self.user1 = "Tik"
        self.user2 = "Tok"
        self.turn = "Tik"

    def run(self):
        print("How many pencils would you like to use:")
        self.pens = int(input())
        print(f"Who will be the first ({self.user1}, {self.user2}):")
        self.turn = input()
        print(self.pens * "|")
        print(f"{self.turn} is going first!")


pen_paper = PenPaperGame()
pen_paper.run()
