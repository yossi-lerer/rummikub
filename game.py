from tiles import create_pool, dealing_cards, is_valid_set, play_set
from turn import read_player_move, play_turn
from display import display_hand
def play_game():
    table = []
    player, computer, pool = dealing_cards(create_pool())
    player = sorted(player, key=lambda h: h[0])
    while True:
        display_hand("Your hand:", player)
        set = read_player_move(player)
        if set == None:
            play_turn(player, pool, table, set)
        elif is_valid_set(set[1]):
            play_turn(player, pool, table, set[0])
            print(table)

play_game()