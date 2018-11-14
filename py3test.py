import itertools


def win(current_game):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    #Hoz check win
    for row in game:
        print(row)
    if all_same(row):
        print("Player {row[0]} is the winner horizontally!")
        return True


    #Diagonally check in
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print("Player won by diagonally!")
        return True

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        print("Player won by diagonally!")
        return True


    #Vertical check win
    for col in range(len(game)):

        check = []

        for row in game:
            check.append(row[col])
        if all_same(check):
            print("Winner via Row")
            return True

    return False


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] !=0:
            print("This position is taken! Find another one")
            return game_map, False
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print (count, row)
        return game_map, True

    except IndexError as e:
        print ("Error: make sure you input row and column!", e)
        return game_map, False

    except Exception as e:
        print("Something went wrong here!", e)
        return game_map, False

play = True
players = [1,2]
while play:
    game_size = int(input("What game size do you want? 3x3? 10x10? "))
    game = []

    for i in range(game_size):
        row = []
        for i in range(game_size):
            row.append(0)
        game.append(row)

    game_won = False
    # _ means don't care about return
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle([1,2])
    #no one won anything yet
    while not game_won:
        current_player = next(player_choice)
        print("Current player is ___")
        played = False

        while not played:
            column_choice = int(input("What column do you want to play? : "))
            row_choice = int(input("What row do you want to play? : "))
            game, played = game_board(game, current_player, row_choice, column_choice)

        if win(game):
            game_won = True
            again = input("The game is over, would you like to play again? (y/n) ")
            if again.lower() == "y":
                print ("restart game")
            elif again.lower() == "n":
                print ("Bye")
                play = False
            else:
                print("Not valid answer")
                play = False