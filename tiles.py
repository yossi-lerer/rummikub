import random

def create_pool():
    pool = []
    for symbol in ["R", "B", "K", "O"]:
        for num in range(1,14):
            pool.append((num, symbol))
    pool = pool * 2
    random.shuffle(pool)
    return pool

# [(1, R),(2, R),(3, R),(4, R)]
def is_valid_set(tiles):
    tiles = sorted(tiles, key=lambda t: t[0] or t[1])
    
    last_card = tiles[0]
    flag = False
    
    for tile in tiles[1:]:
        if tile[0] == last_card[0] + 1 and tile[1] == last_card[1]:
            flag = True
            last_card = tile
        else:
            flag = False
            break

    if not flag:
        last_card = tiles[0]
        for tile in tiles[1:]:
            if tile[0] == last_card[0]:
                color = 0
                for symbol in tiles:
                    if tile[1] != symbol[1] or color == 0:
                        if tile[1] == symbol[1]:
                            color += 1
                        flag = True
                    else:
                        return False
                last_card = tile
            else:
                return False
    
    return flag


def play_set(hand, table, indexes):
    pass

if __name__ == "__main__":
    print(is_valid_set([(1, "R"),(2, "R"),(3, "R"),(4, "R")]))
    print(is_valid_set([(4, "R"),(4, "B"),(4, "R"),(4, "O")]))
    print(create_pool())