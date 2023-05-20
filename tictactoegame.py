def choose_players():
    player1 = ''
    player2 = ''
    while player1 not in ['X', 'O']:
        player1 = input('Player 1: Do you want  to be X or O?: ')
        if player1 not in ['X', 'O']:
            print('Players can only be X or O, please select again.')
        else:
            player2 = 'O' if player1 == 'X' else 'X' # this is ternary python like in javascript "player1 === 'X' ? player2 = 'O' : player2 = 'X'
    return(player1, player2)

def ready():
    do_players_game = ''
    while do_players_game not in ['Y', 'N']:
        do_players_game = input('Are you ready to play (Y/N)?: ')
        if do_players_game not in ['Y', 'N']:
            print('Your anwers must be Y (Yes) on N (No), please try again.')    
    return True if do_players_game == 'Y' else False

def continue_playing():
    continue_game = ''
    while continue_game not in ['Y', 'N']:
        continue_game = input('Do you want to play again (Y/N)?: ')
        if continue_game not in ['Y', 'N']:
            print('Your anwers must be Y (Yes) on N (No), please try again.')
    return True if continue_game == 'Y' else False

table_game_rows = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
row_separators = '-----------'

def print_panel():
    print(row_separators)
    print(' ' + table_game_rows[0] + ' | ' + table_game_rows[1] + ' | ' + table_game_rows[2])
    print(row_separators)
    print(' ' + table_game_rows[3] + ' | ' + table_game_rows[4] + ' | ' + table_game_rows[5])
    print(row_separators)
    print(' ' + table_game_rows[6] + ' | ' + table_game_rows[7] + ' | ' + table_game_rows[8])
    print(row_separators)

def check_game_status(position_played, player):
    print('position_played: ',position_played)
    print('player: ', players[player])
    if (position_played == 1 and table_game_rows[1] == players[player] and table_game_rows[2] == players[player]):
        return True
    if (position_played == 1 and table_game_rows[4] == players[player] and table_game_rows[8] == players[player]):
        return True
    if (position_played == 1 and table_game_rows[3] == players[player] and table_game_rows[6] == players[player]):
        return True
    if (position_played == 2 and table_game_rows[0] == players[player] and table_game_rows[2] == players[player]):
        return True
    if (position_played == 2 and table_game_rows[4] == players[player] and table_game_rows[7] == players[player]):
        return True
    if (position_played == 3 and table_game_rows[0] == players[player] and table_game_rows[1] == players[player]):
        return True
    if (position_played == 3 and table_game_rows[4] == players[player] and table_game_rows[6] == players[player]):
        return True
    if (position_played == 3 and table_game_rows[5] == players[player] and table_game_rows[8] == players[player]):
        return True
    if (position_played == 4 and table_game_rows[0] == players[player] and table_game_rows[6] == players[player]):
        return True
    if (position_played == 4 and table_game_rows[4] == players[player] and table_game_rows[5] == players[player]):
        return True
    if (position_played == 5 and table_game_rows[0] == players[player] and table_game_rows[8] == players[player]):
        return True
    if (position_played == 5 and table_game_rows[1] == players[player] and table_game_rows[7] == players[player]):
        return True
    if (position_played == 5 and table_game_rows[2] == players[player] and table_game_rows[6] == players[player]):
        return True
    if (position_played == 5 and table_game_rows[3] == players[player] and table_game_rows[5] == players[player]):
        return True
    if (position_played == 6 and table_game_rows[2] == players[player] and table_game_rows[8] == players[player]):
        return True
    if (position_played == 6 and table_game_rows[3] == players[player] and table_game_rows[4] == players[player]):
        return True
    if (position_played == 7 and table_game_rows[0] == players[player] and table_game_rows[3] == players[player]):
        return True
    if (position_played == 7 and table_game_rows[7] == players[player] and table_game_rows[8] == players[player]):
        return True
    if (position_played == 8 and table_game_rows[1] == players[player] and table_game_rows[4] == players[player]):
        return True
    if (position_played == 8 and table_game_rows[6] == players[player] and table_game_rows[8] == players[player]):
        return True
    if (position_played == 9 and table_game_rows[0] == players[player] and table_game_rows[4] == players[player]):
        return True
    if (position_played == 9 and table_game_rows[2] == players[player] and table_game_rows[5] == players[player]):
        return True
    if (position_played == 9 and table_game_rows[6] == players[player] and table_game_rows[7] == players[player]):
        return True
    return False

print('\n'*100) # clear screen
players = choose_players()
are_ready = ready()
player = 0
next_position = 0

if are_ready:
    print('\n'*100) # clear screen
    print(print_panel())
    acceptable_values = range(1,10)
    total_cells_filled =  0
    is_there_a_winner = False
    while total_cells_filled < 9 and is_there_a_winner == False:
        next_position = input('Choose our next position: (1-9): ')
        if next_position.isdigit() == False: 
            print('Your position must be a free cell between 1 and 9, please try again.')
        else:
            if int(next_position) in acceptable_values:
                if table_game_rows[int(next_position) - 1] == ' ':
                    table_game_rows[int(next_position) - 1] = players[player]
                    total_cells_filled = total_cells_filled + 1
                    print('\n'*100) # clear screen
                    is_there_a_winner = check_game_status(int(next_position), player)
                    print('is_there_a_winner: ', is_there_a_winner)
                    print(print_panel())
                    if (is_there_a_winner == False):
                        player = 0 if player == 1 else 1
                    else:
                        print('The winner is player: ', players[player])
                        if (continue_playing() == True):
                            total_cells_filled =  0
                            is_there_a_winner = False
                            table_game_rows = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
                            print('\n'*100) # clear screen
                            print(print_panel())
                else:
                    print('Your position must be a FREE CELL between 1 and 9, please try again.')
            else:
                print('Your position must be a free cell between 1 and 9, please try again.')
    if (total_cells_filled > 8 and is_there_a_winner == False):
        print('The game ended in a tie.')
else:
    print('You left the game, come back when ready!!')