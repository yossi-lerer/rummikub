from tiles import create_pool, dealing_cards, is_valid_set
from turn import read_player_move, play_turn, find_computer_move
from display import display_hand, display_table
def play_game():
    table = []
    player, computer, pool = dealing_cards(create_pool())
    i = 0
    while True:
        if i == 0:
            player = sorted(player, key=lambda h: h[0])
            display_hand("Your hand:", player)
            sets = read_player_move(player)    
            i = 1    
            if sets == None: # type: ignore
                play_turn(player, pool, table, sets)
            elif is_valid_set(sets[1]):
                play_turn(player, pool, table, sets[0]) # type: ignore
                display_table("table:", table)
        
        if i == 1:
            computer = sorted(computer, key=lambda h: h[0])
            display_hand("computer hand:", computer)
            sets = find_computer_move(computer)
            i = 0
            if sets == None: # type: ignore
                play_turn(computer, pool, table, sets)
            elif is_valid_set(sets[1]):
                play_turn(computer, pool, table, sets[0]) # type: ignore
                display_table("table:", table)

play_game()