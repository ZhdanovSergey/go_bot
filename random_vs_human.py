from six.moves import input
import sys

from dlgo.agent import naive
from dlgo import goboard
from dlgo import gotypes
from dlgo.utils import print_board, print_move, point_from_coords, clear_console


board_size = int(sys.argv[1]) if len(sys.argv) == 2 else 9

def main():
	game = goboard.GameState.new_game(board_size)
	bot = naive.RandomBot()
	while not game.is_over():
		clear_console()
		print_board(game.board)
		print()
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