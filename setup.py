def print_board(state: list[str]):
    for i, sign in enumerate(state):
        if i in [2,5,8]:
            print(sign)
        else:
            print(sign, end='')

def read_player_input() -> tuple[str, int]:
    eingabe = "A"
    while eingabe not in ["X", "O"]:
        eingabe = input("Bitte wähle zwischen X oder O aus:\n")

    position = -1
    while position not in range(1,10):
        position = input("Bitte wähle eine Position:\n")
        try:
            position = int(position)
        except:
            print("Cannot convert to integer. Please enter valid input.")
    
    return (eingabe, position)


def update_board(state: list[str], user_input: tuple[str, int]):
    position = user_input[1] - 1
    state[position] = user_input[0]
    return state


def check_for_win(state: list[str], user_input: tuple[str, int]) -> bool:
    state = update_board(state=state, user_input=user_input)
    # check if first row same
    if len(set(state[0:3])) == 1 and set(state[0:3]) != set("#"): 
        return True
    # check second row
    if len(set(state[3:6])) == 1 and set(state[3:6]) != set("#"): 
        return True
    # check third row
    if len(set(state[6:9])) == 1 and set(state[6:9]) != set("#"): 
        return True
    # check first column
    if len(set(state[0::3])) == 1 and set(state[0::3]) != set("#"): 
        return True
    # check second column
    if len(set(state[1::3])) == 1 and set(state[1::3]) != set("#"): 
        return True
    # check third column
    if len(set(state[2::3])) == 1 and set(state[2::3]) != set("#"): 
        return True
    if len(set(state[0::4])) == 1 and set(state[0::4]) != set("#"): 
        return True
    if len(set(state[2::2])) == 1 and set(state[2::2]) != set("#"): 
        return True

    return False

