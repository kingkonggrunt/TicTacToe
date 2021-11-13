from board import TicTacToeBoard
import random

class TicTacToeGame:
    def __init__(self, board: TicTacToeBoard, x_player, o_player):
        self.board = board
        self.x = x_player
        self.x.letter = "X"
        self.o = o_player
        self.o.letter = "O"

    def validate_move(self, move):
        if move is None:
            return False

        if not move.isdigit():
            print("Not a Move. Try Again")
            return False
        elif int(move) not in [i for i in range(9)]:
            print("Invalid Move. Try Again")
            return False
        elif self.board.board[int(move)] != " ":
            print("Invalid Move (Space occupied). Try Again")
            self.board.print_board(show_available_moves=True)
            return False

        return True

    def check_if_winner(self, letter):
        row_win_conds = [[i for i in range(row*3, (row+1)*3)] for row in range(3)]
        # row_wins = [[0,1,2], [3,4,5], [6,7,8]]
        col_win_conds = [[i+col for i in range(0, 9, 3)]for col in range(3)]
        # col_wins = [[0,3,6], [1,4,7], [2,5,8]]
        dia_win_conds = [[0,4,8], [2,4,6]]

        # print([row_win_conds, col_win_conds, dia_win_conds])

        for win_conds in [row_win_conds, col_win_conds, dia_win_conds]:
            for win_cond in win_conds:
                moves = [self.board.board[i] for i in win_cond]
                if moves.count(letter) == len(moves):
                    return True

        return False

    def check_if_draw(self):
        return not " " in self.board.board

    def play(self):
        print("Welcome to TicTacToe")
        winner = False
        draw = False

        turn = random.choice([self.x, self.o])
        print(f"Player {turn.name} goes first. Letter {turn.letter}")

        while (winner == False) and (draw == False):
            self.board.print_board()
            print(f"== Player {turn.name} turn. Letter {turn.letter}")

            move = None
            _validated = self.validate_move(move)
            while not _validated:
                move = turn.make_move()
                _validated = self.validate_move(move)
            self.board.add_move(letter=turn.letter, move=int(move))

            winner = self.check_if_winner(letter=turn.letter)
            draw = self.check_if_draw()

            if turn == self.x:
                turn = self.o
            else:
                turn = self.x

        if winner:
            print("")
            print(f" ===== Player {turn.name} (letter {turn.letter}) has won the game!! =====")
            self.board.print_board()
        elif draw:
            print("")
            print(" ===== Game is a Draw! ===== ")
            self.board.print_board()
