def print_board(state: list[str]):
    for i, sign in enumerate(state):
        if i in [2,5,8]:
            print(sign)
        else:
            print(sign, end='')

def read_player_input():
    eingabe = "A"
    while eingabe not in ["X", "O"]:
        eingabe = input("Bitte wähle zwischen X oder O aus:\n")
    return eingabe

