import time
from dlgo import gotypes, goboard
from dlgo.agent import naive
from dlgo.utils import clear_console, print_board, print_move

def main():
	board_size = 9
	game = goboard.GameState.new_game(board_size)
	bots = {
		gotypes.Player.black: naive.RandomBot(),
		gotypes.Player.white: naive.RandomBot(),
	}
	while not game.is_over():
		time.sleep(0.3)
		clear_console()
		print_board(game.board)
		bot_move = bots[game.next_player].select_move(game)
		print_move(game.next_player, bot_move)
		game = game.apply_move(bot_move)

if __name__ == '__main__':
	main()