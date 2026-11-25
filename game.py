from tiles import create_pool, dealing_cards, is_valid_set, play_set
from turn import read_player_move
def play_game():
    player, computer, pool = dealing_cards(create_pool())
    print(player)
    read_player_move(player)

play_game()