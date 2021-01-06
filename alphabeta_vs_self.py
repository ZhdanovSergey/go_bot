from six.moves import input
import sys
import time

from dlgo import goboard_fast as goboard
from dlgo import gotypes
from dlgo.minimax import alphabeta
from dlgo.utils import print_board, print_move, clear_console


board_size = int(sys.argv[1]) if len(sys.argv) == 2 else 5

def capture_diff(game_state):
    black_stones = 0
    white_stones = 0
    for r in range(1, game_state.board.num_rows + 1):
        for c in range(1, game_state.board.num_cols + 1):
            p = gotypes.Point(r, c)
            color = game_state.board.get(p)
            if color == gotypes.Player.black:
                black_stones += 1
            elif color == gotypes.Player.white:
                white_stones += 1
    diff = black_stones - white_stones
    if game_state.next_player == gotypes.Player.black:
        return diff
    return -1 * diff


def main():
    game = goboard.GameState.new_game(board_size)
    bots = {
        gotypes.Player.black: alphabeta.AlphaBetaAgent(2, capture_diff),
        gotypes.Player.white: alphabeta.AlphaBetaAgent(2, capture_diff),
    }

    while not game.is_over():
        bot_move = bots[game.next_player].select_move(game)
        game = game.apply_move(bot_move)
        clear_console()
        print_board(game.board)
        print_move(game.next_player, bot_move)
        time.sleep(0.1)
    print(game.winner(), 'win')


if __name__ == '__main__':
    main()