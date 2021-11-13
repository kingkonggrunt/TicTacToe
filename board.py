class TicTacToeBoard:
    def __init__(self):
        self.board = [" " for _ in range(9)]

    def print_board(self, show_available_moves=False):

        if show_available_moves:
            for row in range(3):
                current_row = [str(i) if self.board[i] == " " else self.board[i] for i in range(row*3, (row+1)*3)]
                print("|" + "|".join(current_row) + "|")

        else:
            for row in range(3):
                print("|" + "|".join([str(self.board[i]) for i in range(row*3, (row+1)*3)]) + "|")

        print("")
    # def print_moves(self):
        # for row in range(3):
            # print("|" + "|".join([i for i in range(row*3, (row+1)*3)]) + "|")

    def add_move(self, letter, move):
        self.board[move] = letter
