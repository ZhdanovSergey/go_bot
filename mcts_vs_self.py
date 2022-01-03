from six.moves import input
import time
import sys

from dlgo import goboard_fast as goboard
from dlgo import gotypes
from dlgo import mcts
from dlgo.utils import print_board, print_move, point_from_coords, clear_console

board_size = int(sys.argv[1]) if len(sys.argv) == 2 else 5


def main():
    game = goboard.GameState.new_game(board_size)
    bots = {
        gotypes.Player.black: mcts.MCTSAgent(500, temperature=1.4),
        gotypes.Player.white: mcts.MCTSAgent(500, temperature=1.4),
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
