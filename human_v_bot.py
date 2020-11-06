from dlgo.agent import naive
from dlgo import goboard
from dlgo import gotypes
from dlgo.utils import clear_console, print_board, print_move, point_from_coords
from six.moves import input

def main():
	board_size = 9
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

if __name__ == '__main__':
	main()