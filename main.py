import os

places = {
    7: '7', 8: '8', 9: '9',
    4: '4', 5: '5', 6: '6',
    1: '1', 2: '2', 3: '3'
}


def draw_grid(place):
    board = (f"{place[7]}|{place[8]}|{place[9]}\n"
             f"-+-+-\n"
             f"{place[4]}|{place[5]}|{place[6]}\n"
             f"-+-+-\n"
             f"{place[1]}|{place[2]}|{place[3]}\n")

    print(board)


def check_winner(place):
    if (place[7] == place[8] == place[9]) \
            or (place[4] == place[5] == place[6]) \
            or (place[1] == place[2] == place[3]):
        return True

    elif (place[1] == place[4] == place[7]) \
            or (place[2] == place[5] == place[8]) \
            or (place[3] == place[6] == place[9]):
        return True

    elif (place[1] == place[5] == place[9]) \
            or (place[3] == place[5] == place[7]):
        return True


game = True
over = False
turn = 0
player = "1"

while game:

    # reset the screen and draw grid
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_grid(places)

    print('please enter the number on the board you want to place your icon on: ')
    choice = input(f'Player {player} enter a number or "q" to quit: ')

    if choice == 'q':
        game = False

    elif str.isdigit(choice) and int(choice) in places:
        if not places[int(choice)] in {'X', 'O'}:

            if turn % 2 == 0:
                places[int(choice)] = "X"
                turn += 1
                player = "2"

            else:
                places[int(choice)] = "O"
                turn += 1
                player = "1"

    if check_winner(places): game, over = False, True
    if turn > 8:
        print("Tie Game!")
        game = False

os.system('cls' if os.name == 'nt' else 'clear')
draw_grid(places)

if over:
    if turn % 2 == 1:
        print("Player 1 wins!")

    else:
        print("Player 2 wins!")