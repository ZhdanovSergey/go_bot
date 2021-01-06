import sys
import time
from dlgo import gotypes, goboard_fast as goboard
from dlgo.agent import naive
from dlgo.utils import clear_console, print_board, print_move


board_size = int(sys.argv[1]) if len(sys.argv) == 2 else 9

def main():
	game = goboard.GameState.new_game(board_size)
	bots = {
		gotypes.Player.black: naive.RandomBot(),
		gotypes.Player.white: naive.RandomBot(),
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