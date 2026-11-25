# [(1, "R"),(2, "R"),(3, "R"),(4, "R")]
def read_player_move(hand):
    while True:
        player_choose = input("Enter card positions to create a set. for example (1 2 3 or D to Draw): ")
        if player_choose.strip() == "D":
            return None
        player_choose = sorted([num - 1 for num in list(map(int, player_choose.split()))])
        if len(player_choose) == len(set(player_choose)):
            if player_choose[-1] < len(hand):
                return player_choose

def find_computer_move(hand):
    pass

def play_turn(hand, pool, table, move):
    pass

if __name__ == "__main__":
    print(read_player_move([(1, "R"),(1, "k"),(1, "R")]))