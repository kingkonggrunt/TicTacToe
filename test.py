from board import TicTacToeBoard
from player import TicTacToePlayer
from game import TicTacToeGame


def main():
    # ## Testing Board
    # b = TicTacToeBoard()
    # b.print_board()
    # b.print_board(show_available_moves=True)
    # b.add_move("X", move=2)
    # b.print_board(show_available_moves=True)
    # b.add_move("X", move=7)
    # b.print_board(show_available_moves=True)
    # b.add_move("O", move=8)
    # # b.add_move("0", move=11)
    # b.print_board(show_available_moves=True)
    #
    # ## Testing player
    # p = TicTacToePlayer(name="DANK EMEME")
    # print(p.name)
    # p.make_move()

    # return None

    ## Testing game
    b = TicTacToeBoard()
    x_player = TicTacToePlayer(name="Player X")
    o_player = TicTacToePlayer(name="Player O")

    game = TicTacToeGame(b, x_player, o_player)
    # game.check_if_winner(letter="X")

    game.play()



if __name__ == "__main__":
    main()
    # p = TicTacToePlayer(name="DANK EMEME")
    # print(p.name)
    # p.make_move()
