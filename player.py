class TicTacToePlayer:
    def __init__(self, name="Default"):
        self.name=name
        pass

    def make_move(self):
        move = input("Input Move (0-8)")
        return move
