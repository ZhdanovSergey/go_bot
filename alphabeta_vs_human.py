from six.moves import input
import sys

from dlgo import goboard_fast as goboard
from dlgo import gotypes
from dlgo.minimax import alphabeta
from dlgo.utils import print_board, print_move, point_from_coords, clear_console


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
    bot = alphabeta.AlphaBetaAgent(2, capture_diff)

    while not game.is_over():
        clear_console()
        print_board(game.board)
        if not game.previous_state is None:
            prev_game = game.previous_state
            if not prev_game.previous_state is None:
                print_move(prev_game.previous_state.next_player, prev_game.last_move)
            print_move(game.previous_state.next_player, game.last_move)
        if game.next_player == gotypes.Player.black:
            human_move = input('-- ')
            point = point_from_coords(human_move.strip())
            move = goboard.Move.play(point)
        else:
            move = bot.select_move(game)
        game = game.apply_move(move)
    print(game.winner(), 'win')


if __name__ == '__main__':
    main()