import sys

from setup import check_for_win, print_board, read_player_input, update_board

if __name__ == "__main__":
    win = False
    state = ["#"] * 9

    while not win:
        print_board(state=state)
        user_input = read_player_input()
        if check_for_win(state=state, user_input=user_input):
            state = update_board(state=state, user_input=user_input)
            print_board(state=state)
            print("Winner!")
            sys.exit()
        state = update_board(state=state, user_input=user_input)