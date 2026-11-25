from tiles import play_set
# [(1, "R"),(2, "R"),(3, "R"),(4, "R")]
def read_player_move(hand):
    while True:
        player_choose = input("Choose tile positions or D to draw. for example (1 2 3 or D to Draw): ")
        if player_choose.strip() == "D":
            return None
        player_choose = sorted([num - 1 for num in list(map(int, player_choose.split()))])
        if len(player_choose) == len(set(player_choose)):
            if player_choose[-1] < len(hand):
                cards = [hand[i] for i in player_choose]
                return player_choose, cards
        print("Invalid set. Try again.")

def find_computer_move(hand):
    pass

def play_turn(hand, pool, table, move):
    if move != None:
        play_set(hand, table, move)
    else:
        hand.append(pool.pop())

if __name__ == "__main__":
    print(read_player_move([(1, "R"),(1, "k"),(1, "R")]))