def print_board(state: list[str]):
    for i, sign in enumerate(state):
        if i in [2,5,8]:
            print(sign)
        else:
            print(sign, end='')
